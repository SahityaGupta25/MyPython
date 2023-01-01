class A:
    def __init__(self) :
        self.m1=66

class B:
    def __init__(self) :
        self.m2=16
class C(B,A):
    def __init__(self) :
        super().__init__()
        self.m3=25

q1=C()
print(q1.m1)
print(q1.m2)