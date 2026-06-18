import os
from token import Token
import re

class Lexer:
    tokens = []
    defaultLocation = os.path.join("prototype", os.path.join("tests", "test.prot"))

    @staticmethod
    def lexFile(file = defaultLocation):
        lineCount = 1

        with open(file, "r") as f:
            for line in f.readlines():
                line = line.replace("(", " ( ").replace(")", " ) ")
                line = re.sub(r"\s+", " ", line).strip()

                for tok in line.split(" "):
                    tok = tok.strip()
                    Lexer.tokens.append(Token.evaluateToken(tok, lineCount))
                    print(Lexer.tokens[-1].tokenType, Lexer.tokens[-1].value, Lexer.tokens[-1].linePos)

                lineCount += 1
        
        print(Lexer.tokens)

lex = Lexer()
lex.lexFile()