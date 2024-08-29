import org.antlr.v4.runtime.tree.TerminalNode;

public class EvalVisitor extends CalculadoraBaseVisitor<Double> {

    @Override
    public Double visitExpr(CalculadoraParser.ExprContext ctx) {
        // Manejo de operaciones binarias
        if (ctx.op != null) {
            double left = visit(ctx.expr(0));
            double right = visit(ctx.expr(1));
            switch (ctx.op.getType()) {
                case CalculadoraParser.MUL:
                    return left * right;
                case CalculadoraParser.DIV:
                    return left / right;
                case CalculadoraParser.ADD:
                    return left + right;
                case CalculadoraParser.SUB:
                    return left - right;
                default:
                    throw new RuntimeException("Operador desconocido: " + ctx.op.getText());
            }
        }

        // Manejo de operaciones con paréntesis
        if (ctx.children.get(0).getText().equals("(") && ctx.children.get(2).getText().equals(")")) {
            return visit(ctx.expr(0));
        }

        // Manejo de la operación ABS
        if (ctx.children.size() == 3 && ctx.children.get(0).getText().equals("abs")) {
            return Math.abs(visit(ctx.expr(0)));
        }

        // Manejo de números
        if (ctx.NUMERO() != null) {
            return Double.parseDouble(ctx.NUMERO().getText());
        }

        throw new RuntimeException("Expresión desconocida: " + ctx.getText());
    }
    
    @Override
    public Double visitTerminal(TerminalNode node) {
        if (node.getSymbol().getType() == CalculadoraParser.NUMERO) {
            return Double.parseDouble(node.getText());
        }
        return super.visitTerminal(node);
    }
}
