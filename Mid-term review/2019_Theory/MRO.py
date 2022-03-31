class O:
    def foo(self, i):
        return i

class A(O):
    def foo(self, i):
        return super().foo(i + 1)

class B(O):
    def foo(self, i):
        return super().foo(i * 2)

class C(O):
    def foo(self, i):
        return super().foo(i * i)

class D(A, B, C):
    def foo(self, i):
        return i * super().foo(i)

class E(D, B):
    def foo(self, i):
        return i + super().foo(i)

class F(B, C, A):
    pass

f = F()
print(f.foo(3))