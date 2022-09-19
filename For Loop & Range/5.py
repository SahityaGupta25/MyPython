# 5. Write a python script to print first N odd natural numbers in reverse order
# =================================================================================

for a in range(int(input("Enter a Number\t"))*2,0,-1):
    if (a%2!=0):
        print(a,end=' ')