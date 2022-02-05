# As in the previous question, when a task is added into expression classes, new methods are added into these classes. 
# Please change the way these classes are implemented in such a way that these classes do not change their contents when new tasks are added into these classes: 

# - Define class Eval to calculate the value of an expression
# - Define class PrintPrefix to return the string corresponding to the expression in prefix format
# - Define class PrintPostfix to return the string corresponding to the expression in postfix format

# Let x be an object expressing an expression, x.accept(Eval()) will return the value of the expression x, 
# x.accept(PrintPrefix()) will return the expression in prefix format and x.accept(PrintPostfix()) will return the expression in postfix format. 

# Be careful that you are not allowed to use type(), isinstance() when implementing this exercise 
# Tip: Use Visitor pattern.

class IntLit:
    def __init__(self, intlit):
        self.intlit = intlit

    def accept(self, visitor):
        return visitor.visit(self)

    def eval(self, visitor):
        return self.intlit
    def printPrefix(self, visitor):
        return self.intlit
    def printPostfix(self, visitor):
        return self.intlit


class FloatLit:
    def __init__(self, floatlit):
        self.floatlit = floatlit

    def accept(self, visitor):
        return visitor.visit(self)

    def eval(self, visitor):
        return self.floatlit
    def printPrefix(self, visitor):
        return self.floatlit
    def printPostfix(self, visitor):
        return self.floatlit

class BinExp:
    def __init__(self, i1, exp, i2):
        self.i1 = i1
        self.exp = exp
        self.i2 = i2

    def accept(self, visitor):
        return visitor.visit(self)

    def eval(self, visitor):
        if self.exp == '+':
            return self.i1.eval(visitor) + self.i2.eval(visitor)
        elif self.exp == '-':
            return self.i1.eval(visitor) - self.i2.eval(visitor)
        elif self.exp == '*':
            return self.i1.eval(visitor) * self.i2.eval(visitor)
        elif self.exp == '/':
            return self.i1.eval(visitor) / self.i2.eval(visitor)


    def printPrefix(self, visitor):
        return self.exp + ' ' + str(self.i1.eval(visitor)) + ' ' + str(self.i2.eval(visitor))
    def printPostfix(self, visitor):
        return str(self.i1.eval(visitor)) + ' ' + str(self.i2.eval(visitor)) + ' ' + self.exp

class UnExp:
    def __init__(self, exp, i):
        self.i = i
        self.exp = exp

    def accept(self, visitor):
        return visitor.visit(self)

    def eval(self, visitor):
        if self.exp == '+':
            return self.i.eval(visitor)
        elif self.exp == '-':
            return -1*self.i.eval(visitor)
    def printPrefix(self, visitor):
        return self.exp + '. ' + str(self.i.eval(visitor))
    def printPostfix(self, visitor):
        return str(self.i.eval(visitor)) + ' ' + self.exp + '.'

class Visitor:
    pass

class Eval(Visitor):
    def visit(self, crop):
        return crop.eval(self)

class PrintPrefix(Visitor):
    def visit(self, crop):
        return crop.printPrefix(self)

class PrintPostfix(Visitor):
    def visit(self, crop):
        return crop.printPostfix(self)

x1 = IntLit(1)
x2 = FloatLit(2.0)
x3 = BinExp(IntLit(1), "+", IntLit(1))
x4 = UnExp("-", IntLit(1))
x5 = BinExp(UnExp("-", IntLit(1)), "+", BinExp(IntLit(4), "*", FloatLit(2.0)))

# x5 = BinExp(-1, +, BinExp(4, *, 2.0)).accept(PrintPrefix)

print(x1.accept(Eval()))
print(x1.accept(PrintPrefix()))
print(x1.accept(PrintPostfix()))

print("-------------------------------")

print(x2.accept(Eval()))
print(x2.accept(PrintPrefix()))
print(x2.accept(PrintPostfix()))

print("-------------------------------")

print(x3.accept(Eval()))
print(x3.accept(PrintPrefix()))
print(x3.accept(PrintPostfix()))

print("-------------------------------")

print(x4.accept(Eval()))
print(x4.accept(PrintPrefix()))
print(x4.accept(PrintPostfix()))

print("-------------------------------")

print(x5.accept(Eval()))
print(x5.accept(PrintPrefix()))
print(x5.accept(PrintPostfix()))