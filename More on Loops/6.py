# 6. Write a python script to print first N prime numbers
# =========================================================


num=int(input("Enter a Number\t"))
print("Prime Numbers are =",end=' ')
for n in range(1,num):
    for i in range(2,n):
        if (n%i==0):
            break
    else :
        print(n,end=' ')
