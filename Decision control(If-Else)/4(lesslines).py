'''
# 4. Write a python script to print greater between two numbers. Print number only once even if the numbers are the same.
# ---------------------------------------------------------------------

x=int(input("Enter Value of X.\t"))
y=int(input("Enter value of Y.\t"))
if (x>y):
    print("X is greater than Y")
elif (y>x):
    print("Y is greater than X")
elif(x==y):
    print("Both Values are Same")
'''

# Answer in less Lines of Code

x,y=int(input("Enter a Number\n")),int(input("Enter a Number\n"))
print(x if x>y else y)


