# 6. Write a python program to check whether a given string is a multiword string or single word string using match case statement
# ----------------------------------------------------------------


x=input("Enter 1st \n")
y=input("Enter 2nd String\n")
match x,y:
    case _:
        if (len(x)>len(y)):
            print("1st String is Multiword String")
        else :
            print("2nd String is Multiword String")