# 9. Write a python script to check whether a given year is a leap year or not.
# --------------------------------------------------------------------

x=int(input("Enter a Year"))
if (x%100 and x%4):
    print("Not Leap Yearr")
else:
    print("Leap Year")