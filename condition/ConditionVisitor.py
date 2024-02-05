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


    # Visit a parse tree produced by ConditionParser#Print.
    def visitPrint(self, ctx:ConditionParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConditionParser#LessThan.
    def visitLessThan(self, ctx:ConditionParser.LessThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConditionParser#GreaterThan.
    def visitGreaterThan(self, ctx:ConditionParser.GreaterThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConditionParser#Value.
    def visitValue(self, ctx:ConditionParser.ValueContext):
        return self.visitChildren(ctx)



del ConditionParser