# 5. Write a python script to print first N odd natural numbers in reverse order
# --------------------------------------------------------------------------------


n=int(input("Enter a Number"))
n*=2
i=1
while (n>=i):
    if n%2!=0:
        print(n)
    n-=1