from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from Visitor import Visitor

class AST(ABC):
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def accept(self, v, param):
        method_name = 'visit{}'.format(self.__class__.__name__)
        visit = getattr(v, method_name)
        return visit(self, param)

class Type(ABC):
    pass

@dataclass
class MemDecl:
    typ: Type
    var: str

    def __str__(self):
        return "MemDecl(" + str(self.typ) + "," + str(self.var) + ")"

@dataclass
class Struct(Type):
    decl: list[MemDecl]

    def __str__(self):
        return "Struct([" + ','.join(str(i) for i in self.decl) + "])"

class IntType(Type):
    def __str__(self):
        return "IntType"

class FloatType(Type):
    def __str__(self):
        return "FloatType"






