# Generated from baziliolanguage/Bazilio.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,199,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,5,0,40,8,0,
        10,0,12,0,43,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,5,2,52,8,2,10,2,12,
        2,55,9,2,1,3,5,3,58,8,3,10,3,12,3,61,9,3,1,4,1,4,1,4,3,4,66,8,4,
        1,4,1,4,1,4,1,4,3,4,72,8,4,1,4,1,4,3,4,76,8,4,3,4,78,8,4,1,5,1,5,
        1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,106,8,10,1,11,1,11,
        1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,
        1,13,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,144,8,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,5,16,179,8,16,10,16,12,16,182,9,16,1,17,
        5,17,185,8,17,10,17,12,17,188,9,17,1,18,1,18,5,18,192,8,18,10,18,
        12,18,195,9,18,1,18,1,18,1,18,0,1,32,19,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,0,0,211,0,41,1,0,0,0,2,44,1,0,0,0,4,53,
        1,0,0,0,6,59,1,0,0,0,8,77,1,0,0,0,10,79,1,0,0,0,12,83,1,0,0,0,14,
        86,1,0,0,0,16,89,1,0,0,0,18,92,1,0,0,0,20,95,1,0,0,0,22,107,1,0,
        0,0,24,113,1,0,0,0,26,117,1,0,0,0,28,123,1,0,0,0,30,126,1,0,0,0,
        32,143,1,0,0,0,34,186,1,0,0,0,36,189,1,0,0,0,38,40,3,2,1,0,39,38,
        1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,1,1,0,0,0,43,
        41,1,0,0,0,44,45,5,12,0,0,45,46,3,4,2,0,46,47,5,29,0,0,47,48,3,6,
        3,0,48,49,5,30,0,0,49,3,1,0,0,0,50,52,5,14,0,0,51,50,1,0,0,0,52,
        55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,5,1,0,0,0,55,53,1,0,0,
        0,56,58,3,8,4,0,57,56,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,
        1,0,0,0,60,7,1,0,0,0,61,59,1,0,0,0,62,66,3,10,5,0,63,66,3,12,6,0,
        64,66,3,14,7,0,65,62,1,0,0,0,65,63,1,0,0,0,65,64,1,0,0,0,66,78,1,
        0,0,0,67,72,3,16,8,0,68,72,3,18,9,0,69,72,3,20,10,0,70,72,3,22,11,
        0,71,67,1,0,0,0,71,68,1,0,0,0,71,69,1,0,0,0,71,70,1,0,0,0,72,78,
        1,0,0,0,73,76,3,24,12,0,74,76,3,26,13,0,75,73,1,0,0,0,75,74,1,0,
        0,0,76,78,1,0,0,0,77,65,1,0,0,0,77,71,1,0,0,0,77,75,1,0,0,0,78,9,
        1,0,0,0,79,80,5,14,0,0,80,81,5,17,0,0,81,82,3,32,16,0,82,11,1,0,
        0,0,83,84,5,1,0,0,84,85,5,14,0,0,85,13,1,0,0,0,86,87,5,2,0,0,87,
        88,3,32,16,0,88,15,1,0,0,0,89,90,5,10,0,0,90,91,3,32,16,0,91,17,
        1,0,0,0,92,93,5,12,0,0,93,94,3,34,17,0,94,19,1,0,0,0,95,96,5,3,0,
        0,96,97,3,32,16,0,97,98,5,29,0,0,98,99,3,6,3,0,99,105,5,30,0,0,100,
        101,5,4,0,0,101,102,5,29,0,0,102,103,3,6,3,0,103,104,5,30,0,0,104,
        106,1,0,0,0,105,100,1,0,0,0,105,106,1,0,0,0,106,21,1,0,0,0,107,108,
        5,5,0,0,108,109,3,32,16,0,109,110,5,29,0,0,110,111,3,6,3,0,111,112,
        5,30,0,0,112,23,1,0,0,0,113,114,5,14,0,0,114,115,5,9,0,0,115,116,
        3,32,16,0,116,25,1,0,0,0,117,118,5,8,0,0,118,119,5,14,0,0,119,120,
        5,31,0,0,120,121,3,32,16,0,121,122,5,32,0,0,122,27,1,0,0,0,123,124,
        5,11,0,0,124,125,5,14,0,0,125,29,1,0,0,0,126,127,5,14,0,0,127,128,
        5,31,0,0,128,129,3,32,16,0,129,130,5,32,0,0,130,31,1,0,0,0,131,132,
        6,16,-1,0,132,144,3,28,14,0,133,144,3,30,15,0,134,144,3,36,18,0,
        135,136,5,33,0,0,136,137,3,32,16,0,137,138,5,34,0,0,138,144,1,0,
        0,0,139,144,5,14,0,0,140,144,5,16,0,0,141,144,5,15,0,0,142,144,5,
        13,0,0,143,131,1,0,0,0,143,133,1,0,0,0,143,134,1,0,0,0,143,135,1,
        0,0,0,143,139,1,0,0,0,143,140,1,0,0,0,143,141,1,0,0,0,143,142,1,
        0,0,0,144,180,1,0,0,0,145,146,10,19,0,0,146,147,5,18,0,0,147,179,
        3,32,16,20,148,149,10,18,0,0,149,150,5,19,0,0,150,179,3,32,16,19,
        151,152,10,17,0,0,152,153,5,20,0,0,153,179,3,32,16,18,154,155,10,
        16,0,0,155,156,5,21,0,0,156,179,3,32,16,17,157,158,10,15,0,0,158,
        159,5,22,0,0,159,179,3,32,16,16,160,161,10,14,0,0,161,162,5,25,0,
        0,162,179,3,32,16,15,163,164,10,13,0,0,164,165,5,26,0,0,165,179,
        3,32,16,14,166,167,10,12,0,0,167,168,5,27,0,0,168,179,3,32,16,13,
        169,170,10,11,0,0,170,171,5,28,0,0,171,179,3,32,16,12,172,173,10,
        10,0,0,173,174,5,23,0,0,174,179,3,32,16,11,175,176,10,9,0,0,176,
        177,5,24,0,0,177,179,3,32,16,10,178,145,1,0,0,0,178,148,1,0,0,0,
        178,151,1,0,0,0,178,154,1,0,0,0,178,157,1,0,0,0,178,160,1,0,0,0,
        178,163,1,0,0,0,178,166,1,0,0,0,178,169,1,0,0,0,178,172,1,0,0,0,
        178,175,1,0,0,0,179,182,1,0,0,0,180,178,1,0,0,0,180,181,1,0,0,0,
        181,33,1,0,0,0,182,180,1,0,0,0,183,185,3,32,16,0,184,183,1,0,0,0,
        185,188,1,0,0,0,186,184,1,0,0,0,186,187,1,0,0,0,187,35,1,0,0,0,188,
        186,1,0,0,0,189,193,5,6,0,0,190,192,3,32,16,0,191,190,1,0,0,0,192,
        195,1,0,0,0,193,191,1,0,0,0,193,194,1,0,0,0,194,196,1,0,0,0,195,
        193,1,0,0,0,196,197,5,7,0,0,197,37,1,0,0,0,13,41,53,59,65,71,75,
        77,105,143,178,180,186,193
    ]

class BazilioParser ( Parser ):

    grammarFileName = "Bazilio.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<?>'", "'<w>'", "'if'", "'else'", "'while'", 
                     "'{'", "'}'", "'8<'", "'<<'", "'(:)'", "'#'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'<-'", "'*'", "'/'", "'%'", "'+'", "'-'", "'='", "'/='", 
                     "'>'", "'<'", "'>='", "'<='", "'|:'", "':|'", "'['", 
                     "']'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "CUTTING", "ADDING", "REPRDO", "SIZE", "PROCNAME", 
                      "NOTE", "VAR", "NUM", "STRING", "ASSIGN", "MUL", "DIV", 
                      "MOD", "SUM", "SUB", "EQ", "NEQ", "GT", "LT", "GET", 
                      "LET", "START_BLOCK", "END_BLOCK", "LEFT_BRACKET", 
                      "RIGHT_BRACKET", "LEFT_PARANTHESES", "RIGHT_PARANTHESES", 
                      "COMMENT", "WS" ]

    RULE_root = 0
    RULE_procedureDefinition = 1
    RULE_parametersId = 2
    RULE_instructions = 3
    RULE_instruction = 4
    RULE_assign = 5
    RULE_input_ = 6
    RULE_output_ = 7
    RULE_reprod = 8
    RULE_procedureCall = 9
    RULE_condition = 10
    RULE_while_ = 11
    RULE_addElementToList = 12
    RULE_removeElementFromList = 13
    RULE_sizeFromList = 14
    RULE_query = 15
    RULE_expr = 16
    RULE_parametersExpr = 17
    RULE_list = 18

    ruleNames =  [ "root", "procedureDefinition", "parametersId", "instructions", 
                   "instruction", "assign", "input_", "output_", "reprod", 
                   "procedureCall", "condition", "while_", "addElementToList", 
                   "removeElementFromList", "sizeFromList", "query", "expr", 
                   "parametersExpr", "list" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    CUTTING=8
    ADDING=9
    REPRDO=10
    SIZE=11
    PROCNAME=12
    NOTE=13
    VAR=14
    NUM=15
    STRING=16
    ASSIGN=17
    MUL=18
    DIV=19
    MOD=20
    SUM=21
    SUB=22
    EQ=23
    NEQ=24
    GT=25
    LT=26
    GET=27
    LET=28
    START_BLOCK=29
    END_BLOCK=30
    LEFT_BRACKET=31
    RIGHT_BRACKET=32
    LEFT_PARANTHESES=33
    RIGHT_PARANTHESES=34
    COMMENT=35
    WS=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def procedureDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ProcedureDefinitionContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ProcedureDefinitionContext,i)


        def getRuleIndex(self):
            return BazilioParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = BazilioParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 38
                self.procedureDefinition()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcedureDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROCNAME(self):
            return self.getToken(BazilioParser.PROCNAME, 0)

        def parametersId(self):
            return self.getTypedRuleContext(BazilioParser.ParametersIdContext,0)


        def START_BLOCK(self):
            return self.getToken(BazilioParser.START_BLOCK, 0)

        def instructions(self):
            return self.getTypedRuleContext(BazilioParser.InstructionsContext,0)


        def END_BLOCK(self):
            return self.getToken(BazilioParser.END_BLOCK, 0)

        def getRuleIndex(self):
            return BazilioParser.RULE_procedureDefinition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedureDefinition" ):
                return visitor.visitProcedureDefinition(self)
            else:
                return visitor.visitChildren(self)




    def procedureDefinition(self):

        localctx = BazilioParser.ProcedureDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_procedureDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(BazilioParser.PROCNAME)
            self.state = 45
            self.parametersId()
            self.state = 46
            self.match(BazilioParser.START_BLOCK)
            self.state = 47
            self.instructions()
            self.state = 48
            self.match(BazilioParser.END_BLOCK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(BazilioParser.VAR)
            else:
                return self.getToken(BazilioParser.VAR, i)

        def getRuleIndex(self):
            return BazilioParser.RULE_parametersId

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametersId" ):
                return visitor.visitParametersId(self)
            else:
                return visitor.visitChildren(self)




    def parametersId(self):

        localctx = BazilioParser.ParametersIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_parametersId)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 50
                self.match(BazilioParser.VAR)
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.InstructionContext)
            else:
                return self.getTypedRuleContext(BazilioParser.InstructionContext,i)


        def getRuleIndex(self):
            return BazilioParser.RULE_instructions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstructions" ):
                return visitor.visitInstructions(self)
            else:
                return visitor.visitChildren(self)




    def instructions(self):

        localctx = BazilioParser.InstructionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_instructions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 21806) != 0):
                self.state = 56
                self.instruction()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(BazilioParser.AssignContext,0)


        def input_(self):
            return self.getTypedRuleContext(BazilioParser.Input_Context,0)


        def output_(self):
            return self.getTypedRuleContext(BazilioParser.Output_Context,0)


        def reprod(self):
            return self.getTypedRuleContext(BazilioParser.ReprodContext,0)


        def procedureCall(self):
            return self.getTypedRuleContext(BazilioParser.ProcedureCallContext,0)


        def condition(self):
            return self.getTypedRuleContext(BazilioParser.ConditionContext,0)


        def while_(self):
            return self.getTypedRuleContext(BazilioParser.While_Context,0)


        def addElementToList(self):
            return self.getTypedRuleContext(BazilioParser.AddElementToListContext,0)


        def removeElementFromList(self):
            return self.getTypedRuleContext(BazilioParser.RemoveElementFromListContext,0)


        def getRuleIndex(self):
            return BazilioParser.RULE_instruction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction" ):
                return visitor.visitInstruction(self)
            else:
                return visitor.visitChildren(self)




    def instruction(self):

        localctx = BazilioParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_instruction)
        try:
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [14]:
                    self.state = 62
                    self.assign()
                    pass
                elif token in [1]:
                    self.state = 63
                    self.input_()
                    pass
                elif token in [2]:
                    self.state = 64
                    self.output_()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [10]:
                    self.state = 67
                    self.reprod()
                    pass
                elif token in [12]:
                    self.state = 68
                    self.procedureCall()
                    pass
                elif token in [3]:
                    self.state = 69
                    self.condition()
                    pass
                elif token in [5]:
                    self.state = 70
                    self.while_()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 75
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [14]:
                    self.state = 73
                    self.addElementToList()
                    pass
                elif token in [8]:
                    self.state = 74
                    self.removeElementFromList()
                    pass
                else:
                    raise NoViableAltException(self)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BazilioParser.VAR, 0)

        def ASSIGN(self):
            return self.getToken(BazilioParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(BazilioParser.ExprContext,0)


        def getRuleIndex(self):
            return BazilioParser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = BazilioParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(BazilioParser.VAR)
            self.state = 80
            self.match(BazilioParser.ASSIGN)
            self.state = 81
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Input_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BazilioParser.VAR, 0)

        def getRuleIndex(self):
            return BazilioParser.RULE_input_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInput_" ):
                return visitor.visitInput_(self)
            else:
                return visitor.visitChildren(self)




    def input_(self):

        localctx = BazilioParser.Input_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_input_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(BazilioParser.T__0)
            self.state = 84
            self.match(BazilioParser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Output_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BazilioParser.ExprContext,0)


        def getRuleIndex(self):
            return BazilioParser.RULE_output_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutput_" ):
                return visitor.visitOutput_(self)
            else:
                return visitor.visitChildren(self)




    def output_(self):

        localctx = BazilioParser.Output_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_output_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(BazilioParser.T__1)
            self.state = 87
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReprodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPRDO(self):
            return self.getToken(BazilioParser.REPRDO, 0)

        def expr(self):
            return self.getTypedRuleContext(BazilioParser.ExprContext,0)


        def getRuleIndex(self):
            return BazilioParser.RULE_reprod

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReprod" ):
                return visitor.visitReprod(self)
            else:
                return visitor.visitChildren(self)




    def reprod(self):

        localctx = BazilioParser.ReprodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_reprod)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(BazilioParser.REPRDO)
            self.state = 90
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcedureCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROCNAME(self):
            return self.getToken(BazilioParser.PROCNAME, 0)

        def parametersExpr(self):
            return self.getTypedRuleContext(BazilioParser.ParametersExprContext,0)


        def getRuleIndex(self):
            return BazilioParser.RULE_procedureCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedureCall" ):
                return visitor.visitProcedureCall(self)
            else:
                return visitor.visitChildren(self)




    def procedureCall(self):

        localctx = BazilioParser.ProcedureCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_procedureCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(BazilioParser.PROCNAME)
            self.state = 93
            self.parametersExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BazilioParser.ExprContext,0)


        def START_BLOCK(self, i:int=None):
            if i is None:
                return self.getTokens(BazilioParser.START_BLOCK)
            else:
                return self.getToken(BazilioParser.START_BLOCK, i)

        def instructions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.InstructionsContext)
            else:
                return self.getTypedRuleContext(BazilioParser.InstructionsContext,i)


        def END_BLOCK(self, i:int=None):
            if i is None:
                return self.getTokens(BazilioParser.END_BLOCK)
            else:
                return self.getToken(BazilioParser.END_BLOCK, i)

        def getRuleIndex(self):
            return BazilioParser.RULE_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = BazilioParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(BazilioParser.T__2)
            self.state = 96
            self.expr(0)
            self.state = 97
            self.match(BazilioParser.START_BLOCK)
            self.state = 98
            self.instructions()
            self.state = 99
            self.match(BazilioParser.END_BLOCK)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 100
                self.match(BazilioParser.T__3)
                self.state = 101
                self.match(BazilioParser.START_BLOCK)
                self.state = 102
                self.instructions()
                self.state = 103
                self.match(BazilioParser.END_BLOCK)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BazilioParser.ExprContext,0)


        def START_BLOCK(self):
            return self.getToken(BazilioParser.START_BLOCK, 0)

        def instructions(self):
            return self.getTypedRuleContext(BazilioParser.InstructionsContext,0)


        def END_BLOCK(self):
            return self.getToken(BazilioParser.END_BLOCK, 0)

        def getRuleIndex(self):
            return BazilioParser.RULE_while_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_" ):
                return visitor.visitWhile_(self)
            else:
                return visitor.visitChildren(self)




    def while_(self):

        localctx = BazilioParser.While_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_while_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(BazilioParser.T__4)
            self.state = 108
            self.expr(0)
            self.state = 109
            self.match(BazilioParser.START_BLOCK)
            self.state = 110
            self.instructions()
            self.state = 111
            self.match(BazilioParser.END_BLOCK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddElementToListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BazilioParser.VAR, 0)

        def ADDING(self):
            return self.getToken(BazilioParser.ADDING, 0)

        def expr(self):
            return self.getTypedRuleContext(BazilioParser.ExprContext,0)


        def getRuleIndex(self):
            return BazilioParser.RULE_addElementToList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddElementToList" ):
                return visitor.visitAddElementToList(self)
            else:
                return visitor.visitChildren(self)




    def addElementToList(self):

        localctx = BazilioParser.AddElementToListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_addElementToList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(BazilioParser.VAR)
            self.state = 114
            self.match(BazilioParser.ADDING)
            self.state = 115
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RemoveElementFromListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CUTTING(self):
            return self.getToken(BazilioParser.CUTTING, 0)

        def VAR(self):
            return self.getToken(BazilioParser.VAR, 0)

        def LEFT_BRACKET(self):
            return self.getToken(BazilioParser.LEFT_BRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(BazilioParser.ExprContext,0)


        def RIGHT_BRACKET(self):
            return self.getToken(BazilioParser.RIGHT_BRACKET, 0)

        def getRuleIndex(self):
            return BazilioParser.RULE_removeElementFromList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRemoveElementFromList" ):
                return visitor.visitRemoveElementFromList(self)
            else:
                return visitor.visitChildren(self)




    def removeElementFromList(self):

        localctx = BazilioParser.RemoveElementFromListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_removeElementFromList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(BazilioParser.CUTTING)
            self.state = 118
            self.match(BazilioParser.VAR)
            self.state = 119
            self.match(BazilioParser.LEFT_BRACKET)
            self.state = 120
            self.expr(0)
            self.state = 121
            self.match(BazilioParser.RIGHT_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SizeFromListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIZE(self):
            return self.getToken(BazilioParser.SIZE, 0)

        def VAR(self):
            return self.getToken(BazilioParser.VAR, 0)

        def getRuleIndex(self):
            return BazilioParser.RULE_sizeFromList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSizeFromList" ):
                return visitor.visitSizeFromList(self)
            else:
                return visitor.visitChildren(self)




    def sizeFromList(self):

        localctx = BazilioParser.SizeFromListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_sizeFromList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(BazilioParser.SIZE)
            self.state = 124
            self.match(BazilioParser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BazilioParser.VAR, 0)

        def LEFT_BRACKET(self):
            return self.getToken(BazilioParser.LEFT_BRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(BazilioParser.ExprContext,0)


        def RIGHT_BRACKET(self):
            return self.getToken(BazilioParser.RIGHT_BRACKET, 0)

        def getRuleIndex(self):
            return BazilioParser.RULE_query

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery" ):
                return visitor.visitQuery(self)
            else:
                return visitor.visitChildren(self)




    def query(self):

        localctx = BazilioParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(BazilioParser.VAR)
            self.state = 127
            self.match(BazilioParser.LEFT_BRACKET)
            self.state = 128
            self.expr(0)
            self.state = 129
            self.match(BazilioParser.RIGHT_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BazilioParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MultiplicationContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExprContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExprContext,i)

        def MUL(self):
            return self.getToken(BazilioParser.MUL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplication" ):
                return visitor.visitMultiplication(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(BazilioParser.VAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class ListExpressionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def list_(self):
            return self.getTypedRuleContext(BazilioParser.ListContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListExpression" ):
                return visitor.visitListExpression(self)
            else:
                return visitor.visitChildren(self)


    class NotEqualsToContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExprContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExprContext,i)

        def NEQ(self):
            return self.getToken(BazilioParser.NEQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotEqualsTo" ):
                return visitor.visitNotEqualsTo(self)
            else:
                return visitor.visitChildren(self)


    class GreaterThanOrEqualsToContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExprContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExprContext,i)

        def GET(self):
            return self.getToken(BazilioParser.GET, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreaterThanOrEqualsTo" ):
                return visitor.visitGreaterThanOrEqualsTo(self)
            else:
                return visitor.visitChildren(self)


    class SumContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExprContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExprContext,i)

        def SUM(self):
            return self.getToken(BazilioParser.SUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSum" ):
                return visitor.visitSum(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(BazilioParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class ListSizeContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def sizeFromList(self):
            return self.getTypedRuleContext(BazilioParser.SizeFromListContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListSize" ):
                return visitor.visitListSize(self)
            else:
                return visitor.visitChildren(self)


    class LessThanContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExprContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExprContext,i)

        def LT(self):
            return self.getToken(BazilioParser.LT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessThan" ):
                return visitor.visitLessThan(self)
            else:
                return visitor.visitChildren(self)


    class LessThanOrEqualsToContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExprContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExprContext,i)

        def LET(self):
            return self.getToken(BazilioParser.LET, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessThanOrEqualsTo" ):
                return visitor.visitLessThanOrEqualsTo(self)
            else:
                return visitor.visitChildren(self)


    class SubtractionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExprContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExprContext,i)

        def SUB(self):
            return self.getToken(BazilioParser.SUB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubtraction" ):
                return visitor.visitSubtraction(self)
            else:
                return visitor.visitChildren(self)


    class NumberContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(BazilioParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LEFT_PARANTHESES(self):
            return self.getToken(BazilioParser.LEFT_PARANTHESES, 0)
        def expr(self):
            return self.getTypedRuleContext(BazilioParser.ExprContext,0)

        def RIGHT_PARANTHESES(self):
            return self.getToken(BazilioParser.RIGHT_PARANTHESES, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)


    class GreaterThanContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExprContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExprContext,i)

        def GT(self):
            return self.getToken(BazilioParser.GT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreaterThan" ):
                return visitor.visitGreaterThan(self)
            else:
                return visitor.visitChildren(self)


    class NoteContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOTE(self):
            return self.getToken(BazilioParser.NOTE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNote" ):
                return visitor.visitNote(self)
            else:
                return visitor.visitChildren(self)


    class DivisionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExprContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExprContext,i)

        def DIV(self):
            return self.getToken(BazilioParser.DIV, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivision" ):
                return visitor.visitDivision(self)
            else:
                return visitor.visitChildren(self)


    class EqualsToContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExprContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExprContext,i)

        def EQ(self):
            return self.getToken(BazilioParser.EQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualsTo" ):
                return visitor.visitEqualsTo(self)
            else:
                return visitor.visitChildren(self)


    class QueryExpressionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def query(self):
            return self.getTypedRuleContext(BazilioParser.QueryContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQueryExpression" ):
                return visitor.visitQueryExpression(self)
            else:
                return visitor.visitChildren(self)


    class ModuleContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExprContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExprContext,i)

        def MOD(self):
            return self.getToken(BazilioParser.MOD, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModule" ):
                return visitor.visitModule(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BazilioParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = BazilioParser.ListSizeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 132
                self.sizeFromList()
                pass

            elif la_ == 2:
                localctx = BazilioParser.QueryExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 133
                self.query()
                pass

            elif la_ == 3:
                localctx = BazilioParser.ListExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 134
                self.list_()
                pass

            elif la_ == 4:
                localctx = BazilioParser.ExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 135
                self.match(BazilioParser.LEFT_PARANTHESES)
                self.state = 136
                self.expr(0)
                self.state = 137
                self.match(BazilioParser.RIGHT_PARANTHESES)
                pass

            elif la_ == 5:
                localctx = BazilioParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 139
                self.match(BazilioParser.VAR)
                pass

            elif la_ == 6:
                localctx = BazilioParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 140
                self.match(BazilioParser.STRING)
                pass

            elif la_ == 7:
                localctx = BazilioParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 141
                self.match(BazilioParser.NUM)
                pass

            elif la_ == 8:
                localctx = BazilioParser.NoteContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 142
                self.match(BazilioParser.NOTE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 180
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 178
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = BazilioParser.MultiplicationContext(self, BazilioParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 145
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 146
                        self.match(BazilioParser.MUL)
                        self.state = 147
                        self.expr(20)
                        pass

                    elif la_ == 2:
                        localctx = BazilioParser.DivisionContext(self, BazilioParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 148
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 149
                        self.match(BazilioParser.DIV)
                        self.state = 150
                        self.expr(19)
                        pass

                    elif la_ == 3:
                        localctx = BazilioParser.ModuleContext(self, BazilioParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 151
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 152
                        self.match(BazilioParser.MOD)
                        self.state = 153
                        self.expr(18)
                        pass

                    elif la_ == 4:
                        localctx = BazilioParser.SumContext(self, BazilioParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 154
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 155
                        self.match(BazilioParser.SUM)
                        self.state = 156
                        self.expr(17)
                        pass

                    elif la_ == 5:
                        localctx = BazilioParser.SubtractionContext(self, BazilioParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 157
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 158
                        self.match(BazilioParser.SUB)
                        self.state = 159
                        self.expr(16)
                        pass

                    elif la_ == 6:
                        localctx = BazilioParser.GreaterThanContext(self, BazilioParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 160
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 161
                        self.match(BazilioParser.GT)
                        self.state = 162
                        self.expr(15)
                        pass

                    elif la_ == 7:
                        localctx = BazilioParser.LessThanContext(self, BazilioParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 163
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 164
                        self.match(BazilioParser.LT)
                        self.state = 165
                        self.expr(14)
                        pass

                    elif la_ == 8:
                        localctx = BazilioParser.GreaterThanOrEqualsToContext(self, BazilioParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 166
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 167
                        self.match(BazilioParser.GET)
                        self.state = 168
                        self.expr(13)
                        pass

                    elif la_ == 9:
                        localctx = BazilioParser.LessThanOrEqualsToContext(self, BazilioParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 169
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 170
                        self.match(BazilioParser.LET)
                        self.state = 171
                        self.expr(12)
                        pass

                    elif la_ == 10:
                        localctx = BazilioParser.EqualsToContext(self, BazilioParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 172
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 173
                        self.match(BazilioParser.EQ)
                        self.state = 174
                        self.expr(11)
                        pass

                    elif la_ == 11:
                        localctx = BazilioParser.NotEqualsToContext(self, BazilioParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 175
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 176
                        self.match(BazilioParser.NEQ)
                        self.state = 177
                        self.expr(10)
                        pass

             
                self.state = 182
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ParametersExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExprContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExprContext,i)


        def getRuleIndex(self):
            return BazilioParser.RULE_parametersExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametersExpr" ):
                return visitor.visitParametersExpr(self)
            else:
                return visitor.visitChildren(self)




    def parametersExpr(self):

        localctx = BazilioParser.ParametersExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_parametersExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 183
                    self.expr(0) 
                self.state = 188
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExprContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExprContext,i)


        def getRuleIndex(self):
            return BazilioParser.RULE_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = BazilioParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(BazilioParser.T__5)
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8590059584) != 0):
                self.state = 190
                self.expr(0)
                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 196
            self.match(BazilioParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[16] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 9)
         




