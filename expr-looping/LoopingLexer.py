# Generated from Looping.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,12,72,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,
        6,1,6,1,6,1,7,1,7,1,7,1,8,4,8,52,8,8,11,8,12,8,53,1,9,1,9,5,9,58,
        8,9,10,9,12,9,61,9,9,1,10,1,10,1,10,1,11,4,11,67,8,11,11,11,12,11,
        68,1,11,1,11,0,0,12,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,
        21,11,23,12,1,0,4,1,0,48,57,2,0,65,90,97,122,3,0,48,57,65,90,97,
        122,3,0,9,10,13,13,32,32,74,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,
        0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,
        17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,1,25,1,0,0,0,3,
        30,1,0,0,0,5,36,1,0,0,0,7,38,1,0,0,0,9,40,1,0,0,0,11,42,1,0,0,0,
        13,44,1,0,0,0,15,47,1,0,0,0,17,51,1,0,0,0,19,55,1,0,0,0,21,62,1,
        0,0,0,23,66,1,0,0,0,25,26,5,115,0,0,26,27,5,101,0,0,27,28,5,110,
        0,0,28,29,5,100,0,0,29,2,1,0,0,0,30,31,5,119,0,0,31,32,5,104,0,0,
        32,33,5,105,0,0,33,34,5,108,0,0,34,35,5,101,0,0,35,4,1,0,0,0,36,
        37,5,43,0,0,37,6,1,0,0,0,38,39,5,45,0,0,39,8,1,0,0,0,40,41,5,60,
        0,0,41,10,1,0,0,0,42,43,5,62,0,0,43,12,1,0,0,0,44,45,5,61,0,0,45,
        46,5,61,0,0,46,14,1,0,0,0,47,48,5,33,0,0,48,49,5,61,0,0,49,16,1,
        0,0,0,50,52,7,0,0,0,51,50,1,0,0,0,52,53,1,0,0,0,53,51,1,0,0,0,53,
        54,1,0,0,0,54,18,1,0,0,0,55,59,7,1,0,0,56,58,7,2,0,0,57,56,1,0,0,
        0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,20,1,0,0,0,61,59,
        1,0,0,0,62,63,5,60,0,0,63,64,5,45,0,0,64,22,1,0,0,0,65,67,7,3,0,
        0,66,65,1,0,0,0,67,68,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,70,
        1,0,0,0,70,71,6,11,0,0,71,24,1,0,0,0,4,0,53,59,68,1,6,0,0
    ]

class LoopingLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    ADD = 3
    SUB = 4
    LT = 5
    GT = 6
    EQ = 7
    NEQ = 8
    NUM = 9
    VAR = 10
    ASSIGN = 11
    WS = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'send'", "'while'", "'+'", "'-'", "'<'", "'>'", "'=='", "'!='", 
            "'<-'" ]

    symbolicNames = [ "<INVALID>",
            "ADD", "SUB", "LT", "GT", "EQ", "NEQ", "NUM", "VAR", "ASSIGN", 
            "WS" ]

    ruleNames = [ "T__0", "T__1", "ADD", "SUB", "LT", "GT", "EQ", "NEQ", 
                  "NUM", "VAR", "ASSIGN", "WS" ]

    grammarFileName = "Looping.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


