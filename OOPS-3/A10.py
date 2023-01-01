# Multiple Inheritance ( MRO )
# Method Resolution Order

class A:
    def f1(self):
        print("F1,Class A")
class B:
    def f1(self):
        print("F1,Class B")

    def f2(self):
        print("F2,Class B")
class C(B,A):
    def f3(self):
        print("F3,Class C")
q1=C()
q1.f1()
