# typechecker.py
# Visitor-based type checker for MyLang (Python)

from MyLangParser import MyLangParser
from MyLangVisitor import MyLangVisitor

class Type:
    INTEGER = 'integer'
    REAL = 'real'
    BOOLEAN = 'boolean'
    ERROR = 'error'

    @staticmethod
    def is_numeric(t):
        return t == Type.INTEGER or t == Type.REAL

class TypeCheckerVisitor(MyLangVisitor):
    def __init__(self):
        self.symtab = {}  # name -> Type
        self.errors = []

    def error(self, token, msg):
        line = token.line if token is not None else '?'
        self.errors.append(f'Linha {line}: {msg}')

    # program: statement* EOF ;
    def visitProgram(self, ctx:MyLangParser.ProgramContext):
        for s in ctx.statement():
            self.visit(s)
        return Type.ERROR

    def visitVarDecl(self, ctx:MyLangParser.VarDeclContext):
        name = ctx.ID().getText()
        declared = self.tokenToType(ctx.type().getText())
        if name in self.symtab:
            self.error(ctx.start, f\"Variável '{name}' já declarada.\")
        else:
            self.symtab[name] = declared
        if ctx.expr():
            t = self.visit(ctx.expr())
            if not self.isAssignable(declared, t):
                self.error(ctx.start, f\"Não é possível atribuir {t} a {declared} na variável '{name}'.\")
        return Type.ERROR

    def visitAssignment(self, ctx:MyLangParser.AssignmentContext):
        name = ctx.ID().getText()
        if name not in self.symtab:
            self.error(ctx.start, f\"Variável '{name}' não declarada.\")
            self.visit(ctx.expr())
            return Type.ERROR
        varType = self.symtab[name]
        rhs = self.visit(ctx.expr())
        if not self.isAssignable(varType, rhs):
            self.error(ctx.start, f\"Atribuição inválida: não é possível atribuir {rhs} a {varType} em '{name}'.\")
        return Type.ERROR

    def visitIfStmt(self, ctx:MyLangParser.IfStmtContext):
        cond = self.visit(ctx.expr())
        if cond != Type.BOOLEAN:
            self.error(ctx.start, \"Condicional 'if' espera expressão booleana.\")
        self.visit(ctx.statement(0))
        if ctx.ELSE() and ctx.statement(1):
            self.visit(ctx.statement(1))
        return Type.ERROR

    def visitWhileStmt(self, ctx:MyLangParser.WhileStmtContext):
        cond = self.visit(ctx.expr())
        if cond != Type.BOOLEAN:
            self.error(ctx.start, \"Condicional 'while' espera expressão booleana.\")
        self.visit(ctx.statement())
        return Type.ERROR

    def visitIoStmt(self, ctx:MyLangParser.IoStmtContext):
        if ctx.LEIA():
            idname = ctx.ID().getText()
            if idname not in self.symtab:
                self.error(ctx.start, f\"Variável '{idname}' não declarada em 'leia'.\")
        else:
            for e in ctx.expr():
                self.visit(e)
        return Type.ERROR

    def visitBlock(self, ctx:MyLangParser.BlockContext):
        # no new scope for simplicity
        for s in ctx.statement():
            self.visit(s)
        return Type.ERROR

    # expressions
    def visitLiteralExpr(self, ctx:MyLangParser.LiteralExprContext):
        if ctx.literal().INT_LITERAL():
            return Type.INTEGER
        if ctx.literal().REAL_LITERAL():
            return Type.REAL
        if ctx.literal().TRUE() or ctx.literal().FALSE():
            return Type.BOOLEAN
        return Type.ERROR

    def visitIdExpr(self, ctx:MyLangParser.IdExprContext):
        name = ctx.ID().getText()
        if name not in self.symtab:
            self.error(ctx.start, f\"Variável '{name}' não declarada.\")
            return Type.ERROR
        return self.symtab[name]

    def visitParenExpr(self, ctx:MyLangParser.ParenExprContext):
        return self.visit(ctx.expr())

    def visitUnaryMinus(self, ctx:MyLangParser.UnaryMinusContext):
        t = self.visit(ctx.expr())
        if not Type.is_numeric(t):
            self.error(ctx.start, \"Operador unário '-' aplicado a tipo não numérico.\")
            return Type.ERROR
        return t

    def visitExpr(self, ctx:MyLangParser.ExprContext):
        # binary ops: ctx.op exists when rule matched expr op expr
        if ctx.getChildCount() == 3 and getattr(ctx, 'op', None) is not None:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.op.text
            if op in ('*','/','+','-'):
                if not Type.is_numeric(left) or not Type.is_numeric(right):
                    self.error(ctx.start, 'Operador aritmético com operandos não numéricos.')
                    return Type.ERROR
                if left == Type.INTEGER and right == Type.INTEGER:
                    return Type.INTEGER
                return Type.REAL
            if op in ('<','>','<=','>='):
                if not Type.is_numeric(left) or not Type.is_numeric(right):
                    self.error(ctx.start, 'Operador relacional aplicado a tipo não numérico.')
                    return Type.ERROR
                return Type.BOOLEAN
            if op in ('==','!='):
                if left == Type.ERROR or right == Type.ERROR:
                    return Type.ERROR
                if left == right or (Type.is_numeric(left) and Type.is_numeric(right)):
                    return Type.BOOLEAN
                self.error(ctx.start, f'Comparação inválida entre tipos {left} e {right}')
                return Type.ERROR
        # otherwise delegate
        return super().visitChildren(ctx)

    def tokenToType(self, t):
        if t == 'inteiro': return Type.INTEGER
        if t == 'real': return Type.REAL
        if t == 'booleano': return Type.BOOLEAN
        return Type.ERROR

    def isAssignable(self, target, value):
        if target == Type.ERROR or value == Type.ERROR: return False
        if target == value: return True
        if target == Type.REAL and value == Type.INTEGER: return True
        return False
