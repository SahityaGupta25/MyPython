# 2. Write a python program to store your own information {name, age, gender, so on..}
# ====================================================================================


x={"name","age",'Gender'}
i=1
n=int(input("Enter Value of Your Information\n"))
while (i<=n):
    y=input("add Your Info 1 More time")
    x.add(y)
    i+=1
print(x)