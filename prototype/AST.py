class AST:
    astTypes = {
        "PROGRAM",
        "FUNCTION",
        "BINARYOP",
        "LEFTPARAN",
        "RIGHTPARAN",
        "ASSIGN",
        "NUMBER",
        "END",
    }

    @staticmethod
    def PROGRAM(body):
        return {"type" : "PROGRAM", "body" : body}
    
    @staticmethod
    def FUNCTION(name, body, params):
        return {"type" : "FUNCTION", "name" : name, "params" : params, "body" : body}
    
    @staticmethod
    def BINARYOP(left, operator, right):
        return {"type" : "BINARYOP", "left" : left, "right" : right, "operator" : operator}
    
    @staticmethod
    def ASSIGN(left, right):
        return {"type" : "ASSIGN", "left" : left, "right" : right}
    
    @staticmethod
    def NUMBER(value):
        return {"type": "NUMBER", "value": value}
    
    @staticmethod
    def IDENTIFIER(name):
        return {"type": "IDENTIFIER", "name": name}