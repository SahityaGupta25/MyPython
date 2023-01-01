# Multiple Inheritance 

class A:
    def f1(self):
        print("F1,Class A")
class B:
    def f2(self):
        print("F2,Class B")
class C(A,B):
    def f3(self):
        print("F3,Class C")
q1=C()
q1.f1()
q1.f2()