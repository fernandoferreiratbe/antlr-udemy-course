import sys

from antlr4 import FileStream, CommonTokenStream
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from VariableVisitor import VariableVisitor

input_stream = FileStream(sys.argv[1])
lexer = ExprLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = ExprParser(token_stream)  # parser represents our ast
abstract_syntax_tree = parser.root()

var_visitor = VariableVisitor()
var_visitor.visit(abstract_syntax_tree)
