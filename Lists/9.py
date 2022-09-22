# 9. Write a Python script to create a list of city names taken from the user.
# ==============================================================================


citylist=[]
x=int(input("enter No. of Cities\t"))
for y in range(0,x):
    z=input("Enter names of City\t")
    citylist.append(z)
print(citylist)
