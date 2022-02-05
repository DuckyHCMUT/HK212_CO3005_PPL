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

print(x1.accept(Eval()))
print(x1.accept(PrintPrefix()))
print(x1.accept(PrintPostfix()))

print(x2.accept(Eval()))
print(x2.accept(PrintPrefix()))
print(x2.accept(PrintPostfix()))

print(x3.accept(Eval()))
print(x3.accept(PrintPrefix()))
print(x3.accept(PrintPostfix()))

print(x4.accept(Eval()))
print(x4.accept(PrintPrefix()))
print(x4.accept(PrintPostfix()))

print(x5.accept(Eval()))
print(x5.accept(PrintPrefix()))
print(x5.accept(PrintPostfix()))