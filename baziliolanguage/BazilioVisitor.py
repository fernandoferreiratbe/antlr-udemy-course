# Generated from baziliolanguage/Bazilio.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .BazilioParser import BazilioParser
else:
    from BazilioParser import BazilioParser

# This class defines a complete generic visitor for a parse tree produced by BazilioParser.

class BazilioVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BazilioParser#root.
    def visitRoot(self, ctx:BazilioParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#procedureDefinition.
    def visitProcedureDefinition(self, ctx:BazilioParser.ProcedureDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#parametersId.
    def visitParametersId(self, ctx:BazilioParser.ParametersIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#instructions.
    def visitInstructions(self, ctx:BazilioParser.InstructionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#instruction.
    def visitInstruction(self, ctx:BazilioParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#assign.
    def visitAssign(self, ctx:BazilioParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#input_.
    def visitInput_(self, ctx:BazilioParser.Input_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#output_.
    def visitOutput_(self, ctx:BazilioParser.Output_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#reprod.
    def visitReprod(self, ctx:BazilioParser.ReprodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#procedureCall.
    def visitProcedureCall(self, ctx:BazilioParser.ProcedureCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#condition.
    def visitCondition(self, ctx:BazilioParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#while_.
    def visitWhile_(self, ctx:BazilioParser.While_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#addElementToList.
    def visitAddElementToList(self, ctx:BazilioParser.AddElementToListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#removeElementFromList.
    def visitRemoveElementFromList(self, ctx:BazilioParser.RemoveElementFromListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#sizeFromList.
    def visitSizeFromList(self, ctx:BazilioParser.SizeFromListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#query.
    def visitQuery(self, ctx:BazilioParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#expr.
    def visitExpr(self, ctx:BazilioParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#parametersExpr.
    def visitParametersExpr(self, ctx:BazilioParser.ParametersExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#list.
    def visitList(self, ctx:BazilioParser.ListContext):
        return self.visitChildren(ctx)



del BazilioParser