import sys

from antlr4 import FileStream, CommonTokenStream
from LoopingLexer import LoopingLexer
from LoopingParser import LoopingParser
from LoopingImplVisitor import LoopingImplVisitor


input_stream = FileStream(sys.argv[1])
lexer = LoopingLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = LoopingParser(token_stream)
abstract_syntax_tree = parser.root()

visitor = LoopingImplVisitor()
visitor.visit(abstract_syntax_tree)
