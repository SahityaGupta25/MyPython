'''
# For loop for characters
f=open("stuff.txt","r")
x=f.read()
for y in x:
    print(y,end='   ')
'''
#  For loop for lines
f=open("stuff.txt","r")
for y in f:
    print(y,end='   ')

