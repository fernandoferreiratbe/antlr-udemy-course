# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,5,29,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,13,
        8,0,11,0,12,0,14,1,1,1,1,1,2,1,2,1,3,1,3,1,4,4,4,24,8,4,11,4,12,
        4,25,1,4,1,4,0,0,5,1,1,3,2,5,3,7,4,9,5,1,0,2,1,0,48,57,2,0,10,10,
        32,32,30,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,
        0,0,1,12,1,0,0,0,3,16,1,0,0,0,5,18,1,0,0,0,7,20,1,0,0,0,9,23,1,0,
        0,0,11,13,7,0,0,0,12,11,1,0,0,0,13,14,1,0,0,0,14,12,1,0,0,0,14,15,
        1,0,0,0,15,2,1,0,0,0,16,17,5,42,0,0,17,4,1,0,0,0,18,19,5,43,0,0,
        19,6,1,0,0,0,20,21,5,45,0,0,21,8,1,0,0,0,22,24,7,1,0,0,23,22,1,0,
        0,0,24,25,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,27,1,0,0,0,27,28,
        6,4,0,0,28,10,1,0,0,0,3,0,14,25,1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUM = 1
    MUL = 2
    PLUS = 3
    SUB = 4
    WS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'*'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "MUL", "PLUS", "SUB", "WS" ]

    ruleNames = [ "NUM", "MUL", "PLUS", "SUB", "WS" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


