import os
import token

class Lexer:
    tokens = {}
    defaultLocation = os.path.join("prototype", os.path.join("tests", "test.prot"))

    @staticmethod
    def lexFile(file = defaultLocation):
        lineCount = 1
        
        with open(file, "r") as f:
            for line in f.readlines():
                
                for tok in line.split(" "):
                    Lexer.tokens[lineCount] = Lexer.tokens.get(lineCount) or []
                    Lexer.tokens[lineCount].append(token.Token.evaluateToken(tok, lineCount))

                lineCount += 1
        
        print(Lexer.tokens)

lex = Lexer()
lex.lexFile()