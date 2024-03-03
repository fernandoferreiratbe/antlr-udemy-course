import sys

from antlr4 import CommonTokenStream, FileStream
from ConditionLexer import ConditionLexer
from ConditionParser import ConditionParser
from EvalConditionVisitor import EvalConditionVisitor


input_stream = FileStream(sys.argv[1])
lexer = ConditionLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = ConditionParser(token_stream)
tree = parser.root()

visitor = EvalConditionVisitor()
visitor.visit(tree)
