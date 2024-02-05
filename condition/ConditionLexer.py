# Generated from Condition.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,45,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,
        3,1,3,1,4,1,4,1,5,4,5,35,8,5,11,5,12,5,36,1,6,4,6,40,8,6,11,6,12,
        6,41,1,6,1,6,0,0,7,1,1,3,2,5,3,7,4,9,5,11,6,13,7,1,0,2,1,0,48,57,
        2,0,10,10,32,32,46,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,
        0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,1,15,1,0,0,0,3,18,1,0,0,
        0,5,23,1,0,0,0,7,29,1,0,0,0,9,31,1,0,0,0,11,34,1,0,0,0,13,39,1,0,
        0,0,15,16,5,105,0,0,16,17,5,102,0,0,17,2,1,0,0,0,18,19,5,101,0,0,
        19,20,5,108,0,0,20,21,5,115,0,0,21,22,5,101,0,0,22,4,1,0,0,0,23,
        24,5,112,0,0,24,25,5,114,0,0,25,26,5,105,0,0,26,27,5,110,0,0,27,
        28,5,116,0,0,28,6,1,0,0,0,29,30,5,62,0,0,30,8,1,0,0,0,31,32,5,60,
        0,0,32,10,1,0,0,0,33,35,7,0,0,0,34,33,1,0,0,0,35,36,1,0,0,0,36,34,
        1,0,0,0,36,37,1,0,0,0,37,12,1,0,0,0,38,40,7,1,0,0,39,38,1,0,0,0,
        40,41,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,43,1,0,0,0,43,44,6,
        6,0,0,44,14,1,0,0,0,3,0,36,41,1,6,0,0
    ]

class ConditionLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    GT = 4
    LT = 5
    NUM = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'print'", "'>'", "'<'" ]

    symbolicNames = [ "<INVALID>",
            "GT", "LT", "NUM", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "GT", "LT", "NUM", "WS" ]

    grammarFileName = "Condition.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


