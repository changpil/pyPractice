## Method Resolution Order


class A:
    def func(self):
        return 'A.func'

class B(A):
    def func(self):
        return 'B.func'

class C(A):
    def func(self):
        return 'C.func'

class D( B, C):
    pass

class E( C, B):
    pass


print(D.mro())
d = D()
print(d.func())


print(E.mro())
e = E()
print(e.func())