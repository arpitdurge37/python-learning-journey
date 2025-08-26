class A:
    def showA(self): print("AAA")

class B(A):
    def showB(self): print("BBB")

b = B()
b.showA()
b.showB()
