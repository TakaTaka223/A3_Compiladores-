from ExecutorVisitor import Executor
from MyLangParser import MyLangParser
import ast
import sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    # Py2/algumas builds podem não ter reconfigure; ignorar nesse caso
    pass


class MyLangRunner(Executor):
    def __init__(self):
        self.memory = {}  # armazena variáveis

    # programa = várias declarações
    def visitProgram(self, ctx: MyLangParser.ProgramContext):
        for stmt in ctx.statement():
            self.visit(stmt)
        return None

    # declaração de variável
    def visitVarDecl(self, ctx: MyLangParser.VarDeclContext):
        name = ctx.ID().getText()
        value = None
        if ctx.expr():
            value = self.visit(ctx.expr())
        self.memory[name] = value
        return None

    # atribuição
    def visitAssignment(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[name] = value
        return value

        # operação de leitura/escrita
    def visitIoStmt(self, ctx: MyLangParser.IoStmtContext):
        first = ctx.getChild(0).getText()
        if first == 'leia':
            var_name = ctx.ID().getText()
            val = input(f"Digite o valor de {var_name}: ")
            try:
                val = float(val) if '.' in val else int(val)
            except ValueError:
                pass
            self.memory[var_name] = val
        elif first == 'escreva':
            values = [self.visit(e) for e in ctx.expr()]
            # converte None para 'None' e garante str
            texto = " ".join(str(v) for v in values)
            # imprime com stdout já configurado como utf-8
            print(texto)
        return None



    # expressões matemáticas
    def visitAddSubExpr(self, ctx: MyLangParser.AddSubExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '+':
            return left + right
        else:
            return left - right

    def visitMulDivExpr(self, ctx: MyLangParser.MulDivExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '*':
            return left * right
        else:
            return left / right

    # literais e identificadores
    def visitLiteralExpr(self, ctx: MyLangParser.LiteralExprContext):
        return self.visit(ctx.literal())

    def visitIdExpr(self, ctx):
        name = ctx.ID().getText()
        if name in self.memory:
            return self.memory[name]
        else:
            print(f"Erro: variável '{name}' não declarada.")
            return None

    def visitLiteral(self, ctx: MyLangParser.LiteralContext):
    # inteiros
        if ctx.INT_LITERAL():
            return int(ctx.INT_LITERAL().getText())
        # reais
        if ctx.REAL_LITERAL():
            return float(ctx.REAL_LITERAL().getText())
        # booleanos
        if ctx.TRUE():
            return True
        if ctx.FALSE():
            return False
        # strings — usa ast.literal_eval para interpretar escapes sem quebrar unicode
        if hasattr(ctx, 'STRING_LITERAL') and ctx.STRING_LITERAL():
            raw = ctx.STRING_LITERAL().getText()   # inclui as aspas, ex: "\"O\\ntexto\""
            try:
                # ast.literal_eval interpreta escapes (e preserva unicode)
                value = ast.literal_eval(raw)
            except Exception:
                # fallback: remove aspas manualmente (menos seguro)
                value = raw[1:-1]
            return value
        return None

    # estrutura de repetição (while)
    def visitWhileStmt(self, ctx: MyLangParser.WhileStmtContext):
        max_iter = 10000  # evita loop infinito
        count = 0
        while self.visit(ctx.expr()):
            stmt = ctx.statement()
            if isinstance(stmt, list):  # pode ser lista ou único statement
                for s in stmt:
                    self.visit(s)
            else:
                self.visit(stmt)
            count += 1
            if count > max_iter:
                print("Erro: loop infinito detectado, encerrando execução.")
                break
        return None
    
    def visitCompExpr(self, ctx: MyLangParser.CompExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text

        if op == '<':
            return left < right
        elif op == '>':
            return left > right
        elif op == '<=':
            return left <= right
        elif op == '>=':
            return left >= right
        elif op == '==':
            return left == right
        elif op == '!=':
            return left != right
        
    def visitEscrevaStmt(self, ctx):
        valores = [self.visit(expr) for expr in ctx.expr()]
        # Garante que strings com acentos sejam mostradas corretamente
        texto = " ".join(str(v) for v in valores)
        import sys
        sys.stdout.reconfigure(encoding='utf-8')
        print(texto)