class A:
    def foo(self):
        print("A")

class B(A):
    pass

class C(B):
    pass

class D(A):
    def foo(self):
        print("D")

class E(A):
    pass

class F(D, E):
    def foo(self):
        print("F")

class G(C,F,D):
    pass

x = G()
x.foo()
print(G.mro())

# G -> C -> B -> F -> D -> E -> A