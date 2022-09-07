''' 
Write a Python Program to Calculate Factorial of a Given Number.
'''


fact=int(input("Enter a Number"))
i=1
while (fact>0):
    i=fact*i
    fact-=1
print(i)

