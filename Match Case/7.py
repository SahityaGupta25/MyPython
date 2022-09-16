# 7. Write a python program to check whether a given number is positive, negative or zero using match case statement
# --------------------------------------------------------------------


x=int(input("Enter a Number\n"))
match x:
    case _:
        if (x>0):
            print("Positive")
        elif (x==0):
            print("Zero")
        else:
            print("Negative")