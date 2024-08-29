// Generated from Calculadora.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CalculadoraParser}.
 */
public interface CalculadoraListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CalculadoraParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(CalculadoraParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link CalculadoraParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(CalculadoraParser.ExprContext ctx);
}