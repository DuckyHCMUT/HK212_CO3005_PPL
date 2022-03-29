# To express an arithmetic expression, there are 5 following classes:
# Exp: general arithmetic expression
# BinExp: an arithmetic expression that contains one binary operators (+,-,*,/) and two operands
# UnExp: an arithmetic expression that contains one unary operator (+,-) and one operand
# IntLit: an arithmetic expression that contains one integer number
# FloatLit: an arithmetic expression that contains one floating point number

# Define these classes in Python (their parents, attributes, methods) such that their objects can response to eval() message by returning the value of the expression. 
# For example, let object x express the arithmetic expression 3 + 4 * 2.0, x.eval() must return 11.0

# Done
from abc import ABC

class Exp(ABC):
    def eval(self):
        pass

class IntLit(int):
    def __init__(self, intlit):
        self.intlit = intlit
    def eval(self):
        return self.intlit

class FloatLit(float):
    def __init__(self, floatlit):
        self.floatlit = floatlit
    def eval(self):
        return self.floatlit

class BinExp(Exp):
    def __init__(self, i1, exp, i2):
        self.i1 = i1
        self.exp = exp
        self.i2 = i2

    def eval(self):
        if self.exp == '+':
            return self.i1.eval() + self.i2.eval()
        elif self.exp == '-':
            return self.i1.eval() - self.i2.eval()
        elif self.exp == '*':
            return self.i1.eval() * self.i2.eval()
        elif self.exp == '/':
            return self.i1.eval() / self.i2.eval()

class UnExp(Exp):
    def __init__(self, exp, i):
        self.i = i
        self.exp = exp

    def eval(self):
        return self.i.eval() if self.exp == '+' else -self.i.eval()


x1 = IntLit(1)
print(x1.eval())

x2 = FloatLit(2.0)
print(x2.eval())

x3 = BinExp(IntLit(1), "+", IntLit(1))
print(x3.eval())

x4 = UnExp("-", IntLit(1))
print(x4.eval())

x5 = BinExp(UnExp("-", IntLit(1)), "+", BinExp(IntLit(4), "*", FloatLit(2.0)))
print(x5.eval())