# 10. Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.
# ----------------------------------------------------------------------

x=int(input("Enter Value of X.\t"))
y=int(input("Enter value of Y.\t"))
z=int(input("Enter value of Z.\t"))
if (x>y and x>z):
    print("X is greater")
elif (y>x and y>z):
    print("Y is greater")
elif (z>x and z>y):
    print("Z is Greater")
elif(x==y==z):
    print("All Values are Same")