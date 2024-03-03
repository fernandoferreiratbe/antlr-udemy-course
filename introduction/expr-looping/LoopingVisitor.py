# Generated from Looping.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LoopingParser import LoopingParser
else:
    from LoopingParser import LoopingParser

# This class defines a complete generic visitor for a parse tree produced by LoopingParser.

class LoopingVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LoopingParser#root.
    def visitRoot(self, ctx:LoopingParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LoopingParser#instructions.
    def visitInstructions(self, ctx:LoopingParser.InstructionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LoopingParser#instruction.
    def visitInstruction(self, ctx:LoopingParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LoopingParser#output.
    def visitOutput(self, ctx:LoopingParser.OutputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LoopingParser#assign.
    def visitAssign(self, ctx:LoopingParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LoopingParser#while_.
    def visitWhile_(self, ctx:LoopingParser.While_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LoopingParser#Sub.
    def visitSub(self, ctx:LoopingParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LoopingParser#LessThan.
    def visitLessThan(self, ctx:LoopingParser.LessThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LoopingParser#Equals.
    def visitEquals(self, ctx:LoopingParser.EqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LoopingParser#Variable.
    def visitVariable(self, ctx:LoopingParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LoopingParser#NumValue.
    def visitNumValue(self, ctx:LoopingParser.NumValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LoopingParser#GreaterThan.
    def visitGreaterThan(self, ctx:LoopingParser.GreaterThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LoopingParser#Sum.
    def visitSum(self, ctx:LoopingParser.SumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LoopingParser#NotEquals.
    def visitNotEquals(self, ctx:LoopingParser.NotEqualsContext):
        return self.visitChildren(ctx)



del LoopingParser