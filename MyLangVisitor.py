# Generated from MyLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MyLangParser import MyLangParser
else:
    from MyLangParser import MyLangParser

# This class defines a complete generic visitor for a parse tree produced by MyLangParser.

class MyLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyLangParser#program.
    def visitProgram(self, ctx:MyLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#statement.
    def visitStatement(self, ctx:MyLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#varDecl.
    def visitVarDecl(self, ctx:MyLangParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#assignment.
    def visitAssignment(self, ctx:MyLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#ifStmt.
    def visitIfStmt(self, ctx:MyLangParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#whileStmt.
    def visitWhileStmt(self, ctx:MyLangParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#ioStmt.
    def visitIoStmt(self, ctx:MyLangParser.IoStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#block.
    def visitBlock(self, ctx:MyLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#type.
    def visitType(self, ctx:MyLangParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:MyLangParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#IdExpr.
    def visitIdExpr(self, ctx:MyLangParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#LiteralExpr.
    def visitLiteralExpr(self, ctx:MyLangParser.LiteralExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#UnaryMinus.
    def visitUnaryMinus(self, ctx:MyLangParser.UnaryMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#CompExpr.
    def visitCompExpr(self, ctx:MyLangParser.CompExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#ParenExpr.
    def visitParenExpr(self, ctx:MyLangParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:MyLangParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#literal.
    def visitLiteral(self, ctx:MyLangParser.LiteralContext):
        return self.visitChildren(ctx)



del MyLangParser