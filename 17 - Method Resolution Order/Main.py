class A:
    def show(self):
        print("menampilkan A")

class B:
    def show(self):
        print("menampilkan B")

class C(A, B):
    pass

Object = C()

Object.show()
# help(Object) 