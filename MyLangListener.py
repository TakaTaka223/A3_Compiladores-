# Generated from MyLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MyLangParser import MyLangParser
else:
    from MyLangParser import MyLangParser

# This class defines a complete listener for a parse tree produced by MyLangParser.
class MyLangListener(ParseTreeListener):

    # Enter a parse tree produced by MyLangParser#program.
    def enterProgram(self, ctx:MyLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by MyLangParser#program.
    def exitProgram(self, ctx:MyLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by MyLangParser#statement.
    def enterStatement(self, ctx:MyLangParser.StatementContext):
        pass

    # Exit a parse tree produced by MyLangParser#statement.
    def exitStatement(self, ctx:MyLangParser.StatementContext):
        pass


    # Enter a parse tree produced by MyLangParser#varDecl.
    def enterVarDecl(self, ctx:MyLangParser.VarDeclContext):
        pass

    # Exit a parse tree produced by MyLangParser#varDecl.
    def exitVarDecl(self, ctx:MyLangParser.VarDeclContext):
        pass


    # Enter a parse tree produced by MyLangParser#assignment.
    def enterAssignment(self, ctx:MyLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MyLangParser#assignment.
    def exitAssignment(self, ctx:MyLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MyLangParser#ifStmt.
    def enterIfStmt(self, ctx:MyLangParser.IfStmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#ifStmt.
    def exitIfStmt(self, ctx:MyLangParser.IfStmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#whileStmt.
    def enterWhileStmt(self, ctx:MyLangParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#whileStmt.
    def exitWhileStmt(self, ctx:MyLangParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#ioStmt.
    def enterIoStmt(self, ctx:MyLangParser.IoStmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#ioStmt.
    def exitIoStmt(self, ctx:MyLangParser.IoStmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#block.
    def enterBlock(self, ctx:MyLangParser.BlockContext):
        pass

    # Exit a parse tree produced by MyLangParser#block.
    def exitBlock(self, ctx:MyLangParser.BlockContext):
        pass


    # Enter a parse tree produced by MyLangParser#type.
    def enterType(self, ctx:MyLangParser.TypeContext):
        pass

    # Exit a parse tree produced by MyLangParser#type.
    def exitType(self, ctx:MyLangParser.TypeContext):
        pass


    # Enter a parse tree produced by MyLangParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:MyLangParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:MyLangParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#IdExpr.
    def enterIdExpr(self, ctx:MyLangParser.IdExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#IdExpr.
    def exitIdExpr(self, ctx:MyLangParser.IdExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#LiteralExpr.
    def enterLiteralExpr(self, ctx:MyLangParser.LiteralExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#LiteralExpr.
    def exitLiteralExpr(self, ctx:MyLangParser.LiteralExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#UnaryMinus.
    def enterUnaryMinus(self, ctx:MyLangParser.UnaryMinusContext):
        pass

    # Exit a parse tree produced by MyLangParser#UnaryMinus.
    def exitUnaryMinus(self, ctx:MyLangParser.UnaryMinusContext):
        pass


    # Enter a parse tree produced by MyLangParser#CompExpr.
    def enterCompExpr(self, ctx:MyLangParser.CompExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#CompExpr.
    def exitCompExpr(self, ctx:MyLangParser.CompExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#ParenExpr.
    def enterParenExpr(self, ctx:MyLangParser.ParenExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#ParenExpr.
    def exitParenExpr(self, ctx:MyLangParser.ParenExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:MyLangParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:MyLangParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#literal.
    def enterLiteral(self, ctx:MyLangParser.LiteralContext):
        pass

    # Exit a parse tree produced by MyLangParser#literal.
    def exitLiteral(self, ctx:MyLangParser.LiteralContext):
        pass



del MyLangParser