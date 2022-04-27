from abc import ABC, abstractmethod, ABCMeta
from Visitor import Visitor

class AST(ABC):
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def accept(self, v, param):
        method_name = 'visit{}'.format(self.__class__.__name__)
        visit = getattr(v, method_name)
        return visit(self, param)


class Type(ABC):
    __metaclass__ = ABCMeta
    pass

class IntType(Type):
    def __str__(self): 
        return "IntType"

class FloatType(Type): 
    def __str__(self): 
        return "FloatType"

class Id:
    #value:string
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Id(" + self.name + ")"

class VarDecl: 
    variable: Id
    varType: Type

    def __init__(self, variable, varType):
        self.variable = variable
        self.varType = varType

    def __str__(self):
        return "VarDecl(" + str(self.variable) + "," + str(self.varType) + ")"

class Program:
    decl: list[VarDecl]

    def __init__(self, decl):
        self.decl = decl

    def __str__(self):
        return "Program([" + ','.join(str(i) for i in self.decl) + "])"