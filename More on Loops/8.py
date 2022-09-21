# 8. Write a python script to print first N terms of a Fibonacci series
# ========================================================================


nterms=int(input("Enter a Number\t"))
n1,n2=1,0
i=0
while (i<=nterms):
    nth=n1+n2
    n1=n2
    n2=nth
    print(nth)
    i+=1