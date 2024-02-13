import sys

from antlr4 import FileStream, CommonTokenStream
from ConditionLexer import ConditionLexer
from ConditionParser import ConditionParser
from EvalConditionVisitor import EvalConditionVisitor

input_stream = FileStream(sys.argv[1])

lexer = ConditionLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = ConditionParser(token_stream)

tree = parser.root()

eval_condition_visitor = EvalConditionVisitor()
eval_condition_visitor.visit(tree)

