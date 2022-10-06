'''
# 6. Write a python script to check whether a given number is a three digit number or not.
# -------------------------------------------------------------------

x=int(input("Enter a No.\n"))
if (x>99 and x<1000):
    print("Three Digit No.")
else:
    print("Not 3 Digit no.")
'''
# Answer in One Line

x=int(input("Enter a Number\t"))
print("Yes this Number is a 3 Digit Number" if 99<x<1000 else "Not 3 digit")