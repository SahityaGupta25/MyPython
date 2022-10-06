'''
# 5. Write a python script to print two given words in dictionary order
# ---------------------------------------------------------------------
x=(input("Enter Value of 1st word\t"))
y=(input("Enter value of 2nd word\t"))
if (x>y):
    print(y)
    print(x)
else :
    print(x)
    print(y)
'''
# Answer in less lines of Code

x,y=input("Enter a word\n"),input("Enter a word\n")
print((y,x) if x>y else (x,y))
