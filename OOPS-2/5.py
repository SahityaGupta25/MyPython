# 5. Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu,hdd) and 2 methods (showConfig() to print the values, __init__() to initialize the values).

class Laptop:
    def __init__(self,a,b,c,d) :
        self.brand= a 
        self.ram= b
        self.cpu= c
        self.HDD= d
    
    def showConfig(self) :
        print(self.brand,self.ram,self.cpu,self.HDD,sep='\n')


xyz=Laptop('ASUS','16GB','i7','500GB')
xyz.showConfig()

