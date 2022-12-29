# 2. Write a python program to create 3 user objects and find the youngest of all.


class user():
   def __init__(self,x) :
    self.age=x
    self.age=x
    self.age=x

ram=user(40)
krishna=user(54)
balram=user(27)

abc=(ram.age if ram.age>krishna.age else krishna.age if ram.age>balram.age else balram.age if balram.age > krishna.age else krishna.age)
print(abc)