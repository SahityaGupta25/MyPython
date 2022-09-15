# 8. Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots
# ------------------------------------------------------------------

from cmath import sqrt
import math
a=int(input("Enter Value of a\t"))
b=int(input("Enter Value of b\t"))
c=int(input("Enter Value of c\t"))
delta=b**2-4*a*c
if (delta>0):
    x= (- b + math.sqrt(delta)) / (2 * a)
    y= (- b - math.sqrt(delta)) / (2*a )
    print("Roots are real & Unequal")
elif (delta==0):
    x= - b / (2 * a)
    print("Roots are real & same")
else :
    print("No real Roots are there")