# 11. Write a python script to take the month value in numeric format and display the number of days in it.
# ------------------------------------------------------------------

x=int(input("Enter Number of Month\t"))
if (x==2):
    print("28 Days")
elif (x==1 or x==3 or x==7 or x==8 or x==10 or x==12):
    print("31 Days")
else :
    print("30 Days")
