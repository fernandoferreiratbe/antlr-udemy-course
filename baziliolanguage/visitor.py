import os
import operator
from collections import defaultdict

from utils import notes

if __name__ is not None and "." in __name__:
    from .BazilioParser import BazilioParser
    from .BazilioVisitor import BazilioVisitor
else:
    from BazilioParser import BazilioParser
    from BazilioVisitor import BazilioVisitor


class BazilioException(Exception):
    def __init__(self, message: str):
        self.message = 'Error' + message


class Process:
    def __init__(self, name: str, params: list, instructions: list):
        self.name = name
        self.params = params
        self.instructions = instructions


class Visitor(BazilioVisitor):
    def __init__(self, entry_proc='Main', entry_params=[]):
        self.entry_proc = entry_proc
        self.entry_params = entry_params

        self.procs = []
        self.stack = []
        self.score = []
        self.notes = notes.get_notes()

    def __proc__(self, name, params_values):
        # Error Handling
        if len(self.procs[name].params) != len(params_values):
            raise BazilioException(
                f"In {name} proc was expecting {str(len(self.procs[name].params))} param(s). "
                f"{str(len(params_values))} param(s) given.'"
            )

        proc_args = defaultdict(lambda: 0)
        for param, value in zip(self.procs[name].params, params_values):
            proc_args[param] = value

        self.stack.append(proc_args)       # We push the arguments needed in procedure
        self.visit(self.procs[name].inss)  # We execute the procedure
        self.stack.pop()                   # We pop these arguments no longer needed

    def visitRoot(self, ctx: BazilioParser.RootContext):
        for procedure in list(ctx.getChildren()):
            self.visit(procedure)

    def visitProcedureDefinition(self, ctx: BazilioParser.ProcedureDefinitionContext):
        return super().visitProcedureDefinition(ctx)

    def visitParametersId(self, ctx: BazilioParser.ParametersIdContext):
        param_list = []
        for param in list(ctx.getChildren()):
            param_list.append(param.getText())

        return param_list

    def visitInstructions(self, ctx: BazilioParser.InstructionsContext):
        for instruction in list(ctx.getChildren()):
            self.visit(instruction)

    def visitInstruction(self, ctx: BazilioParser.InstructionContext):
        return self.visitChildren(ctx)

    def visitAssign(self, ctx: BazilioParser.AssignContext):
        return super().visitAssign(ctx)

    def visitInput_(self, ctx: BazilioParser.Input_Context):
        self.stack[-1][ctx.getChild(1).getText()] = int(input())

    def visitOutput_(self, ctx: BazilioParser.Output_Context):
        nodes = list(ctx.getChildren())
        for node in nodes[1:]:
            value = self.visit(node)
            if isinstance(value, list):
                value = str(value)
                value = value.replace(",", "")
                value = value.replace("'", "")
                if node != nodes[-1]:
                    print(value, end=" ")
                else:
                    print(value)
            else:
                if node != nodes[-1]:
                    print(self.visit(node), end=" ")
                else:
                    print(self.visit(node))

    def visitReprod(self, ctx: BazilioParser.ReprodContext):
        return super().visitReprod(ctx)

    def visitProcedureCall(self, ctx: BazilioParser.ProcedureCallContext):
        return super().visitProcedureCall(ctx)

    def visitCondition(self, ctx: BazilioParser.ConditionContext):
        return super().visitCondition(ctx)

    def visitWhile_(self, ctx: BazilioParser.While_Context):
        return super().visitWhile_(ctx)

    def visitAddElementToList(self, ctx: BazilioParser.AddElementToListContext):
        return super().visitAddElementToList(ctx)

    def visitRemoveElementFromList(self, ctx: BazilioParser.RemoveElementFromListContext):
        return super().visitRemoveElementFromList(ctx)

    def visitSizeFromList(self, ctx: BazilioParser.SizeFromListContext):
        return super().visitSizeFromList(ctx)

    def visitQuery(self, ctx: BazilioParser.QueryContext):
        return super().visitQuery(ctx)

    def visitExpr(self, ctx: BazilioParser.ExprContext):
        return super().visitExpr(ctx)

    def visitParametersExpr(self, ctx: BazilioParser.ParametersExprContext):
        param_list = []
        for param in list(ctx.getChildren()):
            param_list.append(self.visit(param))

        return param_list

    def visitList(self, ctx: BazilioParser.ListContext):
        return super().visitList(ctx)
