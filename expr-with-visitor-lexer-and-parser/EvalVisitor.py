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

    def visitSub(self, context: ExprParser.SubContext):
        children = list(context.getChildren())
        return self.visit(children[0]) - self.visit(children[2])

    def visitValue(self, context: ExprParser.ValueContext):
        children = list(context.getChildren())
        return int(children[0].getText())

    def visitSum(self, context: ExprParser.SumContext):
        children = list(context.getChildren())
        return self.visit(children[0]) + self.visit(children[2])
