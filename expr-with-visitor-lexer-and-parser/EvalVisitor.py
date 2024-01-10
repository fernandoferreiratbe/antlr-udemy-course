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
        # Children as only one size represent the NUM from our grammar
        if len(children) == 1:
            return int(children[0].getText())
        else:
            # More thant one represents an expression from our grammar
            if children[1].getText() == '+':
                return self.visit(children[0]) + self.visit(children[2])
            else:
                return self.visit(children[0]) - self.visit(children[2])
