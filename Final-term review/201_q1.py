from abc import ABC
from dataclasses import dataclass

# AST
class AST(ABC):
    pass

class Decl(AST):
    pass

class Type(AST):
    pass

@dataclass
class TypeDecl(Decl):
    name: str
    rhs: Type

    def __init__(self, name, rhs) -> None:
        self.name = name
        self.rhs = rhs

    def __str__(self) -> str:
        return 'TypeDecl(' + '"' + str(self.name) + '",' + str(self.rhs) + ')'

@dataclass
class VarDecl(Decl):
    name: str
    rhs: Type

    def __init__(self, name, rhs) -> None:
        self.name = name
        self.rhs = rhs

    def __str__(self) -> str:
        return 'VarDecl(' + '"' + str(self.name) + '",' + str(self.rhs) + ')'

@dataclass
class Block(Decl):
    ele: list

    def __init__(self, ele) -> None:
        self.ele = ele

    def __str__(self) -> str:
        return 'Block([' + ','.join(str(i) for i in self.ele) + '])'

class IntType(Type):
    def __str__(self) -> str:
        return 'IntType'

class FloatType(Type):
    def __str__(self) -> str:
        return 'FloatType'

@dataclass
class Id(Type):
    name: str

    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return 'Id(' + self.name + ')'


class StaticCheck:
    def __init__(self, input) -> None:
        self.input = input
    
    def check(self) -> str:
        self.visitBlock(self.input, [[IntType(), FloatType()]])
        return "OK"

    def visitBlock(self, ast, o):
        o.append([])
        for i in ast.ele:
            if type(i) == Block:
                self.visitBlock(i, o)
            elif type(i) == VarDecl:
                self.visitVarDecl(i, o)
            elif type(i) == TypeDecl:
                sym = self.visitTypeDecl(i, o)
                o[-1].append(sym)
        o.pop()

    def checkAndRaise(self, left, right):
        if type(left) == type(right):
            return 1
        else:
            if type(left) == Id and type(right) == TypeDecl:
                if str(left.name) == str(right.name):
                    return 1
            return None

    def visitVarDecl(self, ast, o):
        for env in reversed(o):
            for sub_env in env:
                if self.checkAndRaise(ast.rhs, sub_env):
                    return VarDecl(ast.name, ast.rhs)
        print(UndeclaredType(ast.rhs))
            

    def visitTypeDecl(self, ast, o):
        return TypeDecl(ast.name, ast.rhs)

    def visitIntType(self, ast, o):
        return IntType()

    def visitFloatType(self, ast, o):
        return FloatType()

    def visitId(self, ast, o):
        return Id(ast.name)

# Exception
class StaticError(Exception):
    pass

@dataclass
class UndeclaredType(StaticError):
    name: str

    def __str__(self) -> str:
        return "UndeclaredType(" + str(self.name) + ")"


if __name__ == '__main__':
    input = Block([VarDecl("a",IntType()),
            TypeDecl("vd",FloatType()),
            Block([VarDecl("b",FloatType()),
            VarDecl("c",Id("vd"))]),
            Block([VarDecl("d",IntType()),
            TypeDecl("vd1",IntType())]),
            VarDecl("e",Id("vd"))
        ])
        
    x = StaticCheck(input)
    print(x.check())
