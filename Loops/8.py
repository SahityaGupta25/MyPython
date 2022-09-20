# 8. Write a python script to calculate sum of digits of a given number
# =========================================================================

n=int(input("Enter a Number\t"))
sum=0
while (n>0):
    sum=sum+n%10
    n=n//10
print("The sum of Digits are ",sum)