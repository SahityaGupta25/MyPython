# 4. Write a python program to init default values for user object using __init__ method.

class user():
   def __init__(self,x,y,z) :
    self.name=x
    self.age=y
    self.email=z

xyz=user('Lucky',16,'Lucky@yahoo.com')
print(xyz.name)
abc=user('Vasu',18,'Vasu@hotmail.com')


