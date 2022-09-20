# 6. Write a python script to calculate factorial of a given number
# ==================================================================


n=int(input("Enter a Number\t"))
fact=1
i=1
while (i<=n):
    fact=fact*i 
    i+=1
print("factorial of a",n,"is =",fact)