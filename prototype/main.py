from lexer import Lexer
from parser import Parser

lex = Lexer()
lex.lexFile()

parser = Parser(Lexer.tokens)
ast = parser.parse()

print(ast)