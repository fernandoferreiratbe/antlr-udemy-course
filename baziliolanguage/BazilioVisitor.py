# Generated from Bazilio.g4 by ANTLR 4.13.1
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


    # Visit a parse tree produced by BazilioParser#Multiplication.
    def visitMultiplication(self, ctx:BazilioParser.MultiplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Variable.
    def visitVariable(self, ctx:BazilioParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#ListExpression.
    def visitListExpression(self, ctx:BazilioParser.ListExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#NotEqualsTo.
    def visitNotEqualsTo(self, ctx:BazilioParser.NotEqualsToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#GreaterThanOrEqualsTo.
    def visitGreaterThanOrEqualsTo(self, ctx:BazilioParser.GreaterThanOrEqualsToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Sum.
    def visitSum(self, ctx:BazilioParser.SumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#String.
    def visitString(self, ctx:BazilioParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#ListSize.
    def visitListSize(self, ctx:BazilioParser.ListSizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#LessThan.
    def visitLessThan(self, ctx:BazilioParser.LessThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#LessThanOrEqualsTo.
    def visitLessThanOrEqualsTo(self, ctx:BazilioParser.LessThanOrEqualsToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Subtraction.
    def visitSubtraction(self, ctx:BazilioParser.SubtractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Number.
    def visitNumber(self, ctx:BazilioParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Expression.
    def visitExpression(self, ctx:BazilioParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#GreaterThan.
    def visitGreaterThan(self, ctx:BazilioParser.GreaterThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Note.
    def visitNote(self, ctx:BazilioParser.NoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Division.
    def visitDivision(self, ctx:BazilioParser.DivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#EqualsTo.
    def visitEqualsTo(self, ctx:BazilioParser.EqualsToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#QueryExpression.
    def visitQueryExpression(self, ctx:BazilioParser.QueryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Module.
    def visitModule(self, ctx:BazilioParser.ModuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#parametersExpr.
    def visitParametersExpr(self, ctx:BazilioParser.ParametersExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#list.
    def visitList(self, ctx:BazilioParser.ListContext):
        return self.visitChildren(ctx)



del BazilioParser