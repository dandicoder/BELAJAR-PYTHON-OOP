class A:
    def show(self):
        print("menampilkan A")

class B(A):
    def show(self):
        print("menampilkan B")

class C(A):
    def show(self):
        print("menampilkan C")

class D(B, C):
    def show(self):
        print("menampilkan D")

Object = D()

help(Object)