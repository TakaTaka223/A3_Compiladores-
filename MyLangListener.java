// Generated from MyLang.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MyLangParser}.
 */
public interface MyLangListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MyLangParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(MyLangParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLangParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(MyLangParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLangParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(MyLangParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLangParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(MyLangParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLangParser#varDecl}.
	 * @param ctx the parse tree
	 */
	void enterVarDecl(MyLangParser.VarDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLangParser#varDecl}.
	 * @param ctx the parse tree
	 */
	void exitVarDecl(MyLangParser.VarDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLangParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(MyLangParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLangParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(MyLangParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLangParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void enterIfStmt(MyLangParser.IfStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLangParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void exitIfStmt(MyLangParser.IfStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLangParser#whileStmt}.
	 * @param ctx the parse tree
	 */
	void enterWhileStmt(MyLangParser.WhileStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLangParser#whileStmt}.
	 * @param ctx the parse tree
	 */
	void exitWhileStmt(MyLangParser.WhileStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLangParser#ioStmt}.
	 * @param ctx the parse tree
	 */
	void enterIoStmt(MyLangParser.IoStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLangParser#ioStmt}.
	 * @param ctx the parse tree
	 */
	void exitIoStmt(MyLangParser.IoStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLangParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(MyLangParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLangParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(MyLangParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLangParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(MyLangParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLangParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(MyLangParser.TypeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MulDivExpr}
	 * labeled alternative in {@link MyLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterMulDivExpr(MyLangParser.MulDivExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MulDivExpr}
	 * labeled alternative in {@link MyLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitMulDivExpr(MyLangParser.MulDivExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code IdExpr}
	 * labeled alternative in {@link MyLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterIdExpr(MyLangParser.IdExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code IdExpr}
	 * labeled alternative in {@link MyLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitIdExpr(MyLangParser.IdExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LiteralExpr}
	 * labeled alternative in {@link MyLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterLiteralExpr(MyLangParser.LiteralExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LiteralExpr}
	 * labeled alternative in {@link MyLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitLiteralExpr(MyLangParser.LiteralExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code UnaryMinus}
	 * labeled alternative in {@link MyLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterUnaryMinus(MyLangParser.UnaryMinusContext ctx);
	/**
	 * Exit a parse tree produced by the {@code UnaryMinus}
	 * labeled alternative in {@link MyLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitUnaryMinus(MyLangParser.UnaryMinusContext ctx);
	/**
	 * Enter a parse tree produced by the {@code CompExpr}
	 * labeled alternative in {@link MyLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterCompExpr(MyLangParser.CompExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CompExpr}
	 * labeled alternative in {@link MyLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitCompExpr(MyLangParser.CompExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ParenExpr}
	 * labeled alternative in {@link MyLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterParenExpr(MyLangParser.ParenExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ParenExpr}
	 * labeled alternative in {@link MyLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitParenExpr(MyLangParser.ParenExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AddSubExpr}
	 * labeled alternative in {@link MyLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAddSubExpr(MyLangParser.AddSubExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AddSubExpr}
	 * labeled alternative in {@link MyLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAddSubExpr(MyLangParser.AddSubExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLangParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(MyLangParser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLangParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(MyLangParser.LiteralContext ctx);
}