# 11. Write a python script to take the month value in numeric format and display the number of days in it.
# ------------------------------------------------------------------

x=int(input("Enter Number of Month\t"))
if (x==2):
    print("28 Days or 29 Days")
elif x in (1,3,5,7,8,10,12):
    print("31 Days")
elif x in (4,6,9,11):
    print("30 Days")
else :
    print("Invalid Operation")
