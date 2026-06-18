from dataclasses import dataclass, field
from typing import List, Union, Literal

NodeType = Literal[
    "Program",
    "NumericLiteral",
    "Identifier",
    "BinaryExpr",
]

@dataclass
class Stmt:
    kind: NodeType

@dataclass
class Program(Stmt):
    kind: "Program"
    body: List[Stmt] = field(default_factory=list)

@dataclass
class Expression(Stmt):
    pass

@dataclass
class BinaryExpression(Expression):
    kind: "BinaryExpression"
    left: Expression
    right: Expression
    operator: str

@dataclass
class Identifier(Expression):
    kind: "Identifier"
    symbol: str

@dataclass
class NumericLiteral(Expression):
    kind: "Identifier"
    value: float