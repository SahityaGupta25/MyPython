# 2. Write a menu driven program to perform following operations - Addition, Subtraction,Multiplication, Division
# --------------------------------------------------------------------------------------

x=int(input("Press\n1 for Addition\n2 for Substraction\n3 for Multiplication\n4 for Division\n"))
z=int(input("Enter Value of 1st no.\t"))
y=int(input("Enter value of 2nd no.\t"))
match x:
    case 1:
        print(z+y)
    case 2:
        print(z-y)
    case 3:
        print(z*y)
    case 4:
        print(z/y)
    case _:
        print("Ouut of Range")
