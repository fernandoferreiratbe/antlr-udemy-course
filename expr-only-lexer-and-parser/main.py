from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser

input_stream = InputStream(input('? '))

lexer = ExprLexer(input=input_stream)
token_stream = CommonTokenStream(lexer=lexer)
parser = ExprParser(input=token_stream)
tree = parser.root()

print(tree.toStringTree(recog=parser))