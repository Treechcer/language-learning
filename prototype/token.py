class Token:

    keywords = {
        "init" : "INITIALISE",
        "while" : "WHILE"
    }

    def __init__(self, tokenType: str, value: any, linePos: int):
        self.tokenType = tokenType
        self.value = value
        self.linePos = linePos

    @staticmethod
    def evaluateToken(token: str, linePos: int):
        semicolon = token[-1] == ";" or token[-1] == "\n"
        token = token[0:-1] if semicolon else token

        if token.isdigit():
            return Token("NUMBER", int(token), linePos)
        elif token == "+" or token == "-" or token == "*" or token == "/":
            return Token("BINARYOP", token, linePos)
        elif token == "=":
            return Token("EQUALS", token, linePos)
        elif token == "(":
            return Token("LEFTPARAN", token, linePos)
        elif token == ")":
            return Token("RIGHTPARAN", token, linePos)
        elif token == "\n" or semicolon:
            return Token("END", token, linePos)
        
        for i in Token.keywords:
            if token == i:
                return Token(Token.keywords[i], token, linePos)
        
        return Token("INDENTIFIER", token, linePos)