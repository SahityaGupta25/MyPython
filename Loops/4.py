# 4. Write a python script to calculate sum of first N odd natural numbers
# ============================================================================

n=int(input("Enter a Number"))
s=0
for a in range(1,(n*2)+1,2):
    s=s+a
    print(s)
