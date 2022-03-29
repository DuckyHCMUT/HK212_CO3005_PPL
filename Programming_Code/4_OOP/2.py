# Extend the contents of classes Exp, BinExp, UnExp, IntLit, FloatLit such that they can response to printPrefix() message to 
# return the string corresponding to the expression in prefix format. Note that, unary operator +/- is printed as +./-. in prefix format 
# and there is a space after each operator or operand. For example, when receiving message printPrefix(), 
# the object expressing the expression -4 + 3 * 2 will return the string "+ -. 4 * 3 2 "

# Done
from abc import ABC

class Exp(ABC):
    pass 

class IntLit:
    def __init__(self, intlit):
        self.intlit = intlit
    def printPrefix(self):
        return self.intlit

class FloatLit:
    def __init__(self, floatlit):
        self.floatlit = floatlit
    def printPrefix(self):
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

    def printPrefix(self):
        return self.exp + ' ' + str(self.i1.printPrefix()) + ' ' + str(self.i2.printPrefix())

class UnExp(Exp):
    def __init__(self, exp, i):
        self.i = i
        self.exp = exp

    def eval(self):
        if self.exp == '+':
            return +self.i.eval()
        elif self.exp == '-':
            return -self.i.eval()

    def printPrefix(self):
        return self.exp + '. ' + str(self.i.printPrefix())

x1 = IntLit(1)
print(x1.printPrefix())

x2 = FloatLit(2.0)
print(x2.printPrefix())

x3 = BinExp(IntLit(1), "+", IntLit(1))
print(x3.printPrefix())

x4 = UnExp("-", IntLit(1))
print(x4.printPrefix())

x5 = BinExp(UnExp("-", IntLit(1)), "+", BinExp(IntLit(4), "*", FloatLit(2.0)))
print(x5.printPrefix())
