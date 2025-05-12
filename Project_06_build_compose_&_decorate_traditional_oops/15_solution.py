class A:
    def show(self):
        print("A.show() Called")

class B(A):
    def show(self):
        print("B.show() Called")

class C(A):
    def show(self):
        print("C.show() Called")

class D(B, C):
    pass

obj = D()
obj.show()

print(D.__mro__)