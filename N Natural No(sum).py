# Write a Python Program to calculate sum of N Numbers
#------------------------------------------------------


n=int(input("Enter a Number\n"))
sum=0
i=1
while (i<=n):
    sum=sum+i
    i+=1

print("Sum of N Numbers are=",sum)