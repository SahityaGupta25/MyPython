# 1. Write a python program to store all the programming languages known to you using Set.
# =========================================================================================

a=("Enter 3 Languages")
print(a)
z=[]
i=1
while (i<=3):
    x=input( "Enter Programming Language no.\n")
    z.append(x)
    i+=1
y=set(z)    
print(y,end=' ')