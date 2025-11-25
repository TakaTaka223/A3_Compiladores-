from MyLangParser import MyLangParser
from MyLangVisitor import MyLangVisitor

class Executor(MyLangVisitor):
    def __init__(self):
        self.memory = {}

    # Programa
    def visitProgram(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)
        return None

    # Declaração de variável
    def visitVarDecl(self, ctx):
        name = ctx.IDENT().getText()
        value = self.visit(ctx.expr()) if ctx.expr() else None
        self.memory[name] = value
        return None

    # Atribuição
    def visitAssignStmt(self, ctx):
        name = ctx.IDENT().getText()
        value = self.visit(ctx.expr())
        self.memory[name] = value
        return None

    # Escreva
    def visitIoStmt(self, ctx):
        if ctx.getChild(0).getText() == 'escreva':
            value = self.visit(ctx.expr())
            print(value)
        elif ctx.getChild(0).getText() == 'leia':
            name = ctx.IDENT().getText()
            self.memory[name] = input(f"{name} = ")
        return None

    # SE / SENAO
    def visitIfStmt(self, ctx):
        cond = self.visit(ctx.expr())
        if cond:
            self.visit(ctx.statement(0))
        elif ctx.statement(1):
            self.visit(ctx.statement(1))
        return None

    # ENQUANTO
    def visitWhileStmt(self, ctx):
        while self.visit(ctx.expr()):
            self.visit(ctx.statement())
        return None

    # Expressões
    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        return left + right if op == '+' else left - right

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        return left * right if op == '*' else left / right

    def visitComparisons(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        return {
            '>': left > right,
            '>=': left >= right,
            '<': left < right,
            '<=': left <= right,
            '==': left == right,
            '!=': left != right,
        }[op]

    def visitLiteralExpr(self, ctx):
        return self.visit(ctx.literal())

    def visitIdExpr(self, ctx):
        name = ctx.IDENT().getText()
        return self.memory.get(name, None)

    def visitLiteral(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        if ctx.REAL():
            return float(ctx.REAL().getText())
        if ctx.STRING():
            return ctx.STRING().getText().strip('"')
        if ctx.getText() == 'verdadeiro':
            return True
        if ctx.getText() == 'falso':
            return False