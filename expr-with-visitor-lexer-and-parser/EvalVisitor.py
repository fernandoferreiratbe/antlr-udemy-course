if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor


class EvalVisitor(ExprVisitor):
    def visitRoot(self, context: ExprParser.RootContext):
        children = list(context.getChildren())
        print(self.visit(children[0]))

    def visitExpr(self, context: ExprParser.ExprContext):
        children = list(context.getChildren())
        if len(children) == 1:
            return int(children[0].getText())
        else:
            return self.visit(children[0]) + self.visit(children[2])
