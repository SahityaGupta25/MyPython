# Encapsulation

class xyz:
    _a=66 # Protected
    __b=16 # Private
    
    def show(self):
        print(self._a) # Protected
        print(self.__b) # Private

abc=xyz()
abc.show()

print("Outside the program a=",abc._a)
print("Outside the program b=",abc.__b)
