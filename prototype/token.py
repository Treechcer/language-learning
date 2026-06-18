class Token:
    def __init__(self, tokenType: str, value: any, linePos: int):
        self.tokenType = tokenType
        self.value = value
        self.linePos = linePos

    @staticmethod
    def evaluateToken(token: str, linePos: int):
        if token.isdigit():
            return Token("NUMBER", int(token), linePos)
        elif token == "+":
            return Token("ADD", token, linePos)
        elif token == "-":
            return Token("SUB", token, linePos)
        elif token == "=":
            return Token("EQUALS", token, linePos)
        elif token == "\n" or token == ";":
            return Token("END", token, linePos)
        
        return Token("INDENTIFIER", token, linePos)