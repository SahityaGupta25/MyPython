# Write  a Program to Calculate Whether a Given No. is Prime or not.
# -------------------------------------------------------------------



n=(int(input("Enter a Number")))
i=2
while (i<=n-1):
    if (n%i==0):
        break
    i+=1
if (i==n):
    print("Prime")
else :
    print("Composite")