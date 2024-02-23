# Generated from Looping.g4 by ANTLR 4.13.1
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
        4,1,12,68,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,1,5,1,19,8,1,10,1,12,1,22,9,1,1,2,1,2,1,2,3,2,27,
        8,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,3,6,
        43,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,5,6,63,8,6,10,6,12,6,66,9,6,1,6,0,1,12,7,0,2,4,6,8,
        10,12,0,0,70,0,14,1,0,0,0,2,20,1,0,0,0,4,26,1,0,0,0,6,28,1,0,0,0,
        8,31,1,0,0,0,10,35,1,0,0,0,12,42,1,0,0,0,14,15,3,2,1,0,15,16,5,0,
        0,1,16,1,1,0,0,0,17,19,3,4,2,0,18,17,1,0,0,0,19,22,1,0,0,0,20,18,
        1,0,0,0,20,21,1,0,0,0,21,3,1,0,0,0,22,20,1,0,0,0,23,27,3,8,4,0,24,
        27,3,6,3,0,25,27,3,10,5,0,26,23,1,0,0,0,26,24,1,0,0,0,26,25,1,0,
        0,0,27,5,1,0,0,0,28,29,5,1,0,0,29,30,3,12,6,0,30,7,1,0,0,0,31,32,
        5,10,0,0,32,33,5,11,0,0,33,34,3,12,6,0,34,9,1,0,0,0,35,36,5,2,0,
        0,36,37,3,12,6,0,37,38,3,2,1,0,38,11,1,0,0,0,39,40,6,6,-1,0,40,43,
        5,10,0,0,41,43,5,9,0,0,42,39,1,0,0,0,42,41,1,0,0,0,43,64,1,0,0,0,
        44,45,10,8,0,0,45,46,5,3,0,0,46,63,3,12,6,9,47,48,10,7,0,0,48,49,
        5,4,0,0,49,63,3,12,6,8,50,51,10,6,0,0,51,52,5,5,0,0,52,63,3,12,6,
        7,53,54,10,5,0,0,54,55,5,6,0,0,55,63,3,12,6,6,56,57,10,4,0,0,57,
        58,5,7,0,0,58,63,3,12,6,5,59,60,10,3,0,0,60,61,5,8,0,0,61,63,3,12,
        6,4,62,44,1,0,0,0,62,47,1,0,0,0,62,50,1,0,0,0,62,53,1,0,0,0,62,56,
        1,0,0,0,62,59,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,
        65,13,1,0,0,0,66,64,1,0,0,0,5,20,26,42,62,64
    ]

class LoopingParser ( Parser ):

    grammarFileName = "Looping.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'send'", "'while'", "'+'", "'-'", "'<'", 
                     "'>'", "'=='", "'!='", "<INVALID>", "<INVALID>", "'<-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "ADD", "SUB", 
                      "LT", "GT", "EQ", "NEQ", "NUM", "VAR", "ASSIGN", "WS" ]

    RULE_root = 0
    RULE_instructions = 1
    RULE_instruction = 2
    RULE_output = 3
    RULE_assign = 4
    RULE_while_ = 5
    RULE_expression = 6

    ruleNames =  [ "root", "instructions", "instruction", "output", "assign", 
                   "while_", "expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    ADD=3
    SUB=4
    LT=5
    GT=6
    EQ=7
    NEQ=8
    NUM=9
    VAR=10
    ASSIGN=11
    WS=12

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

        def instructions(self):
            return self.getTypedRuleContext(LoopingParser.InstructionsContext,0)


        def EOF(self):
            return self.getToken(LoopingParser.EOF, 0)

        def getRuleIndex(self):
            return LoopingParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = LoopingParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.instructions()
            self.state = 15
            self.match(LoopingParser.EOF)
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
                return self.getTypedRuleContexts(LoopingParser.InstructionContext)
            else:
                return self.getTypedRuleContext(LoopingParser.InstructionContext,i)


        def getRuleIndex(self):
            return LoopingParser.RULE_instructions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstructions" ):
                return visitor.visitInstructions(self)
            else:
                return visitor.visitChildren(self)




    def instructions(self):

        localctx = LoopingParser.InstructionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instructions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 17
                    self.instruction() 
                self.state = 22
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

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
            return self.getTypedRuleContext(LoopingParser.AssignContext,0)


        def output(self):
            return self.getTypedRuleContext(LoopingParser.OutputContext,0)


        def while_(self):
            return self.getTypedRuleContext(LoopingParser.While_Context,0)


        def getRuleIndex(self):
            return LoopingParser.RULE_instruction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction" ):
                return visitor.visitInstruction(self)
            else:
                return visitor.visitChildren(self)




    def instruction(self):

        localctx = LoopingParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.state = 23
                self.assign()
                pass
            elif token in [1]:
                self.state = 24
                self.output()
                pass
            elif token in [2]:
                self.state = 25
                self.while_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(LoopingParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LoopingParser.RULE_output

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutput" ):
                return visitor.visitOutput(self)
            else:
                return visitor.visitChildren(self)




    def output(self):

        localctx = LoopingParser.OutputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_output)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(LoopingParser.T__0)
            self.state = 29
            self.expression(0)
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
            return self.getToken(LoopingParser.VAR, 0)

        def ASSIGN(self):
            return self.getToken(LoopingParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(LoopingParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LoopingParser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = LoopingParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(LoopingParser.VAR)
            self.state = 32
            self.match(LoopingParser.ASSIGN)
            self.state = 33
            self.expression(0)
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

        def expression(self):
            return self.getTypedRuleContext(LoopingParser.ExpressionContext,0)


        def instructions(self):
            return self.getTypedRuleContext(LoopingParser.InstructionsContext,0)


        def getRuleIndex(self):
            return LoopingParser.RULE_while_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_" ):
                return visitor.visitWhile_(self)
            else:
                return visitor.visitChildren(self)




    def while_(self):

        localctx = LoopingParser.While_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_while_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(LoopingParser.T__1)
            self.state = 36
            self.expression(0)
            self.state = 37
            self.instructions()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LoopingParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SubContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LoopingParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LoopingParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LoopingParser.ExpressionContext,i)

        def SUB(self):
            return self.getToken(LoopingParser.SUB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub" ):
                return visitor.visitSub(self)
            else:
                return visitor.visitChildren(self)


    class LessThanContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LoopingParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LoopingParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LoopingParser.ExpressionContext,i)

        def LT(self):
            return self.getToken(LoopingParser.LT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessThan" ):
                return visitor.visitLessThan(self)
            else:
                return visitor.visitChildren(self)


    class EqualsContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LoopingParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LoopingParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LoopingParser.ExpressionContext,i)

        def EQ(self):
            return self.getToken(LoopingParser.EQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquals" ):
                return visitor.visitEquals(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LoopingParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(LoopingParser.VAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class NumValueContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LoopingParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(LoopingParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumValue" ):
                return visitor.visitNumValue(self)
            else:
                return visitor.visitChildren(self)


    class GreaterThanContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LoopingParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LoopingParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LoopingParser.ExpressionContext,i)

        def GT(self):
            return self.getToken(LoopingParser.GT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreaterThan" ):
                return visitor.visitGreaterThan(self)
            else:
                return visitor.visitChildren(self)


    class SumContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LoopingParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LoopingParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LoopingParser.ExpressionContext,i)

        def ADD(self):
            return self.getToken(LoopingParser.ADD, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSum" ):
                return visitor.visitSum(self)
            else:
                return visitor.visitChildren(self)


    class NotEqualsContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LoopingParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LoopingParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LoopingParser.ExpressionContext,i)

        def NEQ(self):
            return self.getToken(LoopingParser.NEQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotEquals" ):
                return visitor.visitNotEquals(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LoopingParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                localctx = LoopingParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 40
                self.match(LoopingParser.VAR)
                pass
            elif token in [9]:
                localctx = LoopingParser.NumValueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 41
                self.match(LoopingParser.NUM)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 64
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 62
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = LoopingParser.SumContext(self, LoopingParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 44
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 45
                        self.match(LoopingParser.ADD)
                        self.state = 46
                        self.expression(9)
                        pass

                    elif la_ == 2:
                        localctx = LoopingParser.SubContext(self, LoopingParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 47
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 48
                        self.match(LoopingParser.SUB)
                        self.state = 49
                        self.expression(8)
                        pass

                    elif la_ == 3:
                        localctx = LoopingParser.LessThanContext(self, LoopingParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 50
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 51
                        self.match(LoopingParser.LT)
                        self.state = 52
                        self.expression(7)
                        pass

                    elif la_ == 4:
                        localctx = LoopingParser.GreaterThanContext(self, LoopingParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 53
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 54
                        self.match(LoopingParser.GT)
                        self.state = 55
                        self.expression(6)
                        pass

                    elif la_ == 5:
                        localctx = LoopingParser.EqualsContext(self, LoopingParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 56
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 57
                        self.match(LoopingParser.EQ)
                        self.state = 58
                        self.expression(5)
                        pass

                    elif la_ == 6:
                        localctx = LoopingParser.NotEqualsContext(self, LoopingParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 59
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 60
                        self.match(LoopingParser.NEQ)
                        self.state = 61
                        self.expression(4)
                        pass

             
                self.state = 66
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         




