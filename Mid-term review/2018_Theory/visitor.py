class A:
    def accept(self, v):
        print("A.accept() was called")
        v.visitA(self)

class B(A):
    def accept(self, v):
        print("B.accept() was called")
        v.visitB(self)

class C:
    def accept(self, v):
        print("C.accept() was called")
        v.visitC(self)

class Visitor:
    def visitA(self, x):
        print("Visitor.visitA() was called")
        return x.accept(self)
    def visitB(self, x):
        print("Visitor.visitB() was called")
        pass
    def visitC(self, x):
        print("Visitor.visitC() was called")
        pass

x = C()
v = Visitor()
v.visitA(x)