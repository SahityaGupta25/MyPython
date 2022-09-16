# 9. Write a python script to check whether a given year is
# a. Non century leap year
# b. Century leap year
# c. Non century non leap year
# d. Century non leap year
# ---------------------------------------------------------------



x=input("Press following keys to see\n'a'= Non century leap year\n'b'= Century leap year\n'c'= Non century non leap year\n'd'= Century non leap year\n")
match x:
    case "a":
        y=int(input("Enter Year Number"))
        if (y%100!=0 and y%4==0):
            print("Non Century Leap Year")
    case "b":
        y=int(input("Enter Year Number"))
        if (y%100==0 and y%400==0):
            print("Century leap year")
    case "c":
        y=int(input("Enter Year Number"))
        if (y%100!=0 and y%400!=0):
            print("Non century non leap year")
    case "d":
        y=int(input("Enter Year Number"))
        if (y%100==0 and y%400!=0):
            print("Century non leap year")
        