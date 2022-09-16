# 4. Write a program which takes user’s age and display the category of person. Age below 10 years- Kid, Age below 20 - Teen, Age below 40 -young, Age below 60 - Experienced, Age above or equal 60 - Senior Citizen.
# -----------------------------------------------------------------------------------------

x=int(input("Enter Age Number\n"))
match x:
    case _:
        if (x<10):
            print("KID")
        elif (x>10 and x<20):
            print("Teen")
        elif (x>20 and x<40):
            print ("Young")
        elif (x>40 and x<60):
            print("Experienced")
        elif (x>=60):
            print("Senior Citizen")