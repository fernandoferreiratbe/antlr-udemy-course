if __name__ is not None and "." in __name__:
    from .ConditionParser import ConditionParser
    from .ConditionVisitor import ConditionVisitor
else:
    from ConditionParser import ConditionParser
    from ConditionVisitor import ConditionVisitor


class EvalConditionVisitor(ConditionVisitor):

    def visitRoot(self, ctx: ConditionParser.RootContext):
        nodes = list(ctx.getChildren())
        for node in nodes:
            self.visit(node)

    def visitCondition(self, ctx: ConditionParser.ConditionContext):
        nodes = list(ctx.getChildren())
        conditional_expression = nodes[1]
        action = nodes[2]
        if self.visit(conditional_expression) == 1:
            self.visit(action)
        elif len(nodes) > 3:
            if ctx.getChild(3).getText() == 'otherwise':
                self.visit(ctx.action(1))

    def visitWrite(self, ctx: ConditionParser.WriteContext):
        nodes = list(ctx.getChildren())
        content = nodes[1]
        print(self.visit(content))

    def visitNext(self, ctx: ConditionParser.NextContext):
        nodes = list(ctx.getChildren())
        value = self.visit(nodes[1]) + 1
        print(value)

    def visitLessThan(self, ctx: ConditionParser.LessThanContext):
        nodes = list(ctx.getChildren())
        return int(self.visit(nodes[0])) < int(self.visit(nodes[2]))

    def visitEquals(self, ctx: ConditionParser.EqualsContext):
        nodes = list(ctx.getChildren())
        return int(self.visit(nodes[0])) == int(self.visit(nodes[2]))

    def visitNumValue(self, ctx: ConditionParser.NumValueContext):
        return int(ctx.NUM().getText())

    def visitGreaterThan(self, ctx: ConditionParser.GreaterThanContext):
        nodes = list(ctx.getChildren())
        return int(self.visit(nodes[0])) > int(self.visit(nodes[2]))

    def visitSum(self, ctx: ConditionParser.SumContext):
        nodes = list(ctx.getChildren())
        return int(self.visit(nodes[0])) + int(self.visit(nodes[2]))

    def visitNotEquals(self, ctx: ConditionParser.NotEqualsContext):
        nodes = list(ctx.getChildren())
        return int(self.visit(nodes[0])) != int(self.visit(nodes[2]))