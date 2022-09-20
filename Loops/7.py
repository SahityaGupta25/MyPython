# 7. Write a python script to count digits in a given number
# =============================================================


n=int(input("Enter a Number:\t"))
i=0
if (n<0):
    n= -1 * n
elif (n==0):
    i=1
while (n!=0):
    n=n//10
    i+=1
print("Count of Digit is =",i)