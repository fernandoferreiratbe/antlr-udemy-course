import operator

if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow
}


class VariableVisitor(ExprVisitor):

    def __init__(self):
        self.expression_vars = {}

    def visitRoot(self, context: ExprParser.RootContext):
        children = list(context.getChildren())
        for index in range(len(children) - 1):
            print(self.visit(children[index]))

    def visitAction(self, context: ExprParser.ActionContext):
        children = list(context.getChildren())

        if len(children) == 3:  # Assignment action
            if children[1].getText() == ':=':
                self.expression_vars[children[0].getText()] = self.visit(children[2])
                return 'assignment to ' + children[0].getText()
            return 'ERROR'
        else:  # len(children) == 2 We have a print
            if children[0].getText() == 'write':
                return str(self.expression_vars[children[1].getText()])
            return 'ERROR'

    def visitExpr(self, context: ExprParser.ExprContext):
        children = list(context.getChildren())
        if len(children) == 1:  # NUM Case
            return int(children[0].getText())
        else:  # len(children) == 3
            return operators[children[1].getText()](
                self.visit(children[0]), self.visit(children[2])
            )
