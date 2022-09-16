# 8. Write a python script to check whether two given strings are identical, first string comes before the second in dictionary order or first string comes after the second string in dictionary order using match case statement
# ----------------------------------------------------------------

x=input("Enter 1st \n")
y=input("Enter 2nd String\n")
match x:
    case _:
        if (x<y):
            print(x)
            print(y)
        else :
            print(y,x,sep="\n")
