if __name__ is not None and "." in __name__:
    from .ConditionParser import ConditionParser
    from .ConditionVisitor import ConditionVisitor
else:
    from ConditionParser import ConditionParser
    from ConditionVisitor import ConditionVisitor


class EvalConditionVisitor(ConditionVisitor):

    def visitRoot(self, context: ConditionParser.RootContext):
        for child in list(context.getChildren()):
            self.visit(child)

    def visitCondition(self, context: ConditionParser.ConditionContext):
        children = list(context.getChildren())

        if self.visit(children[1]) == 1:
            self.visit(context.action(0))
        elif len(children) > 3:
            if context.getChild(3).getText() == 'else':
                self.visit(context.action(1))

    def visitPrint(self, context: ConditionParser.PrintContext):
        children = list(context.getChildren())
        print(self.visit(children[1]))

    def visitLessThan(self, context: ConditionParser.LessThanContext):
        children = list(context.getChildren())
        return int(self.visit(children[0])) < int(self.visit(children[2]))

    def visitGreaterThan(self, context: ConditionParser.GreaterThanContext):
        children = list(context.getChildren())
        return int(self.visit(children[0])) > int(self.visit(children[2]))

    def visitValue(self, context: ConditionParser.ValueContext):
        return int(context.NUM().getText())
