from AST import AST

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
    
    def currentToken(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def shift(self):
        token = self.tokens[self.pos]
        self.pos += 1
        return token

    def parse(self):
        body = []

        while self.currentToken() is not None:
            if self.currentToken().tokenType == "END":
                self.shift()
                continue
            
            statement = self.parseStatement()
            body.append(statement)

        return AST.PROGRAM(body)
    
    def parseStatement(self):
        if self.currentToken().tokenType == "IDENTIFIER":
            if self.pos + 1 < len(self.tokens) and self.tokens[self.pos+1].tokenType == "EQUALS":
                tokenId = self.shift()
                self.shift()
                rightSide = self.expressionParse()

                return AST.ASSIGN(AST.IDENTIFIER(tokenId.value), rightSide)
            
        return self.expressionParse()
    
    def expressionParse(self):
        left = self.parseFactor()

        while self.currentToken() and self.currentToken().tokenType == "BINARYOP" and self.currentToken().value in ("*", "/", "+", "-"):
            operator = self.shift()
            right = self.parseFactor()
            left = AST.BINARYOP(left, operator.value, right)
        
        return left
    
    def parseFactor(self):
        token = self.currentToken()

        if token is None:
            exit(2)

        if token.tokenType == "NUMBER":
            self.shift()
            return AST.NUMBER(token.value)
        elif token.tokenType == "IDENTIFIER":
            self.shift()
            return AST.IDENTIFIER(token.value)
        elif token.tokenType == "LEFTPARAN":
            self.shift()
            expression = self.expressionParse()
            self.shift()
            return expression

        exit(1)