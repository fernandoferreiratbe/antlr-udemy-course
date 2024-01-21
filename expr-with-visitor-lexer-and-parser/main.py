from antlr4 import InputStream, CommonTokenStream
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from EvalVisitor import EvalVisitor

input_stream = InputStream(input("? "))
lexer = ExprLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = ExprParser(token_stream)
abstract_syntax_tree = parser.root()

print(abstract_syntax_tree.toStringTree(recog=parser))

eval_visitor = EvalVisitor()
eval_visitor.visit(abstract_syntax_tree)

print(f"Value read > {input_stream}")
