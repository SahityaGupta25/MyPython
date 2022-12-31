# Add Method

class xyz:
    def __init__(self) : # Instance Method
        self.marks=66
    
    @ staticmethod
    def add(a,b): 
        return a+b

print(xyz.add(3,4))
    # How can we get the answer of x+y 
    # self is not passed also not a cls keyword passed 
    # So these types of Methods are known as Static Methods