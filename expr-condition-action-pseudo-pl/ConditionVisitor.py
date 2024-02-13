# Generated from Condition.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ConditionParser import ConditionParser
else:
    from ConditionParser import ConditionParser

# This class defines a complete generic visitor for a parse tree produced by ConditionParser.

class ConditionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ConditionParser#root.
    def visitRoot(self, ctx:ConditionParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConditionParser#Condition.
    def visitCondition(self, ctx:ConditionParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConditionParser#Write.
    def visitWrite(self, ctx:ConditionParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConditionParser#Next.
    def visitNext(self, ctx:ConditionParser.NextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConditionParser#LessThan.
    def visitLessThan(self, ctx:ConditionParser.LessThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConditionParser#Equals.
    def visitEquals(self, ctx:ConditionParser.EqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConditionParser#NumValue.
    def visitNumValue(self, ctx:ConditionParser.NumValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConditionParser#GreaterThan.
    def visitGreaterThan(self, ctx:ConditionParser.GreaterThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConditionParser#Sum.
    def visitSum(self, ctx:ConditionParser.SumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConditionParser#NotEquals.
    def visitNotEquals(self, ctx:ConditionParser.NotEqualsContext):
        return self.visitChildren(ctx)



del ConditionParser