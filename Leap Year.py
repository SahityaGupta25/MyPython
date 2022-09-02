# Write a Program to check whether this year is a Leap Year or Not
# ----------------------------------------------------------------


x=int(input("Enter a Year"))
if (x%100 and x%4):
    print("Not Leap Yearr")
else:
    print("Leap Year")


