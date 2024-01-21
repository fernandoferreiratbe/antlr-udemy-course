# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#root.
    def visitRoot(self, ctx:ExprParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Sub.
    def visitSub(self, ctx:ExprParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Value.
    def visitValue(self, ctx:ExprParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Sum.
    def visitSum(self, ctx:ExprParser.SumContext):
        return self.visitChildren(ctx)



del ExprParser