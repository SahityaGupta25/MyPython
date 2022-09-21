# 4. Write a python script to print all Prime numbers between two given numbers (both values inclusive)
#  =========================================================================================

n1=int(input("Enter Beginning Value\t"))
n2=int(input("Enter Ending Value\t"))
for x in range (n1,n2):
    for y in range(2,x):
        if (x%y==0):
            break
    else :
        print(x)
