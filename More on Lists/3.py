# 3. Write a Python script to create a list of first N even natural numbers.
# ===========================================================================



mylist=[]
x=int(input("Enter Value of Range\t"))
for a in range(2,x*2+1,2):
    mylist.append(a)
print(mylist)