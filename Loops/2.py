# 2. Write a python script to calculate sum of squares of first N natural numbers
# ================================================================================

n=int(input("Enter a Number\t"))
sq=0
for a in range(1,n+1):
    sq=a**2+sq
    print(sq)