# 2. Write a python script to check whether a given number is Prime or not
# =========================================================================


n=int(input("Enter a Number\t"))
i=2
while (i<=n-1):
    if (n%i==0):
        break
    i+=1
if (i==n):
    print("Prime")
else :
    print("Not Prime")