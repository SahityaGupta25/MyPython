# 3. Write a python script to handle the ArithmeticError

x=25
y=0
try:
    z=x/y
    print("The Value of Division is =",z)
except ArithmeticError:
    print("You have entered Invalid Values")
else:
    print("Division Successful")