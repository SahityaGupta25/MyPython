# 1. Write a python script to reverse a number.
# ================================================

n=int(input("Enter a Number\t"))
if (n!=0):
    a=n%10
    b=n//10
    c=str(a)
    d=str(b)
    print(c+d)
