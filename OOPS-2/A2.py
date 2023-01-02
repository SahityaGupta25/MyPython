# Parameters

class Human:
    v='vasu'
    def __init__(self,x,y,z) :
        self.age=x
        self.gender=y
        self.number=z

    def second(self):
        print(self.age,self.gender)

abc=Human(16,'Male',66)
print(abc.number)

