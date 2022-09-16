'''
3. Write a menu driven program with the following options:
a. Check whether a given set of three numbers are lengths of an isosceles
triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit.
--------------------------------------------------------------------------

'''


tri=input(" 'Press a'. Check whether a given set of three numbers are lengths of an isosceles triangle or not\n 'Press b'. Check whether a given set of three numbers are lengths of sides of a rightangled triangle or not\n 'Press c' Check whether a given set of three numbers are equilateral triangle or not\n 'Press d '. to Exit.\n")
match tri:
    case "a":
        x=int(input("Enter 1st Value\t"))
        y=int(input("Enter 2nd Value\t"))
        z=int(input("Enter 3rd Value\t"))
        if (x==y or y==z or z==x):
            print("three numbers are lengths of an isosceles triangle")
        else :
            print("Not an lengths of an isosceles triangle")
    case "b":
        x=int(input("Enter 1st Value\t"))
        y=int(input("Enter 2nd Value\t"))
        z=int(input("Enter 3rd Value\t"))
        if (x**2+y**2==z**2):
            print("three numbers are lengths of sides of a right angled triangle")
        else :
            print("Not lengths of sides of a right angled triangle")
    case "c":
        x=int(input("Enter 1st Value\t"))
        y=int(input("Enter 2nd Value\t"))
        z=int(input("Enter 3rd Value\t"))
        if (x==y and y==z):
            print("three numbers are equilateral triangle")
        else :
            print("Not an equilateral triangle")
    case "d":
        print("EXIT")

