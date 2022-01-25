# As in the previous question, when a task is added into expression classes, new methods are added into these classes. 
# Please change the way these classes are implemented in such a way that these classes do not change their contents when new tasks are added into these classes: 

# - Define class Eval to calculate the value of an expression
# - Define class PrintPrefix to return the string corresponding to the expression in prefix format
# - Define class PrintPostfix to return the string corresponding to the expression in postfix format

# Let x be an object expressing an expression, x.accept(Eval()) will return the value of the expression x, 
# x.accept(PrintPrefix()) will return the expression in prefix format and x.accept(PrintPostfix()) will return the expression in postfix format. 

# Be careful that you are not allowed to use type(), isinstance() when implementing this exercise 
# Tip: Use Visitor pattern.

from abc import ABC

class Exp(ABC):
    def eval(self):
        pass
    def printPrefix(self):
        pass

class IntLit(int):
    def __init__(self, intlit):
        self.intlit = intlit
    def eval(self):
        return self.intlit
    def printPrefix(self):
        return self.intlit

class FloatLit(float):
    def __init__(self, floatlit):
        self.floatlit = floatlit
    def eval(self):
        return self.floatlit
    def printPrefix(self):
        return self.floatlit


class BinExp(Exp):
    def __init__(self, i1, exp, i2):
        self.i1 = i1
        self.exp = exp
        self.i2 = i2

    def eval(self):
        return self.exp + ' ' + str(self.i1.eval()) + ' ' + str(self.i2.eval())
    def printPrefix(self):
        return self.exp + ' ' + str(self.i1.eval()) + ' ' + str(self.i2.eval())

class UnExp(Exp):
    def __init__(self, exp, i):
        self.i = i
        self.exp = exp

    def eval(self):
        if self.exp == '+':
            return '+. ' + str(self.i.eval())
        elif self.exp == '-':
            return '-. ' + str(self.i.eval())
    def printPrefix(self):
        return self.exp + '. ' + str(self.i.eval())