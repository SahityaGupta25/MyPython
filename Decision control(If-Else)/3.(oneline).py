'''
# 3. Write a python script to check whether a given number is even or odd.
# ------------------------------------------------------------------------

x=int(input("Enter a NO."))
if (x%2==0):
    print("EVEN")
else :
    print("ODD")
'''
# Answer in one line
print("Entered Number is Even" if int(input("Enter a Number\n"))%2==0 else "Entered Number is Odd")