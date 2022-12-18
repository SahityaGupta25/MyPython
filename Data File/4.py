# 4. Write a python script to handle a ValueError

myVar= 66
list = []

try:
   x=list.remove(myVar)
except ValueError:
    print("You are doing it wrong")
else:
    print("The element is removed")
    print(list)
