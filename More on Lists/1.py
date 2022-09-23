# 1. Write a Python script to create a list of first N natural numbers.
# =======================================================================


mylist=[]
x=int(input("Enter Value of Range\t"))
for a in range(1,x+1):
    mylist.append(a)
print(mylist)