if __name__ is not None and "." in __name__:
    from .LoopingParser import LoopingParser
    from .LoopingVisitor import LoopingVisitor
else:
    from LoopingParser import LoopingParser
    from LoopingVisitor import LoopingVisitor


class LoopingImplVisitor(LoopingVisitor):

    def __init__(self):
        variables = {}
        self.stack = []
        self.stack.append(variables)

    def visitRoot(self, context: LoopingParser.RootContext):
        for instructions in list(context.getChildren()):
            self.visit(instructions)

    def visitInstructions(self, context: LoopingParser.InstructionsContext):
        for instruction in list(context.getChildren()):
            self.visit(instruction)

    def visitInstruction(self, context: LoopingParser.InstructionContext):
        return self.visitChildren(context)

    def visitOutput(self, context: LoopingParser.OutputContext):
        nodes = list(context.getChildren())
        print(self.visit(nodes[1]))

    def visitAssign(self, context: LoopingParser.AssignContext):
        nodes = list(context.getChildren())
        self.stack[-1][context.VAR().getText()] = self.visit(nodes[2])

    def visitWhile_(self, context: LoopingParser.While_Context):
        nodes = list(context.getChildren())
        bool_expression = nodes[1]
        actions = nodes[2]
        while self.visit(bool_expression) == 1:
            self.visit(actions)

    def visitSub(self, context: LoopingParser.SubContext):
        nodes = list(context.getChildren())
        return self.visit(nodes[0]) - self.visit(nodes[2])

    def visitLessThan(self, context: LoopingParser.LessThanContext):
        nodes = list(context.getChildren())
        return int(self.visit(nodes[0]) < self.visit(nodes[2]))

    def visitEquals(self, context: LoopingParser.EqualsContext):
        nodes = list(context.getChildren())
        return int(self.visit(nodes[0]) == self.visit(nodes[2]))

    def visitVariable(self, context: LoopingParser.VariableContext):
        return self.stack[-1][context.VAR().getText()]

    def visitNumValue(self, context: LoopingParser.NumValueContext):
        return int(context.NUM().getText())

    def visitGreaterThan(self, context: LoopingParser.GreaterThanContext):
        nodes = list(context.getChildren())
        return int(self.visit(nodes[0]) > self.visit(nodes[2]))

    def visitSum(self, context: LoopingParser.SumContext):
        nodes = list(context.getChildren())
        return self.visit(nodes[0]) + self.visit(nodes[2])

    def visitNotEquals(self, context: LoopingParser.NotEqualsContext):
        nodes = list(context.getChildren())
        return int(self.visit(nodes[0]) != self.visit(nodes[2]))
