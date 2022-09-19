# 1. Write a python script to calculate sum of first N natural numbers
# =======================================================================


n=int(input("Enter a No.\t"))
sum=0
for a in range(1,n+1):
    sum=sum+a
    print(sum)