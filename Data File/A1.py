# Data I/O

'''
r- read
b- binary 
t - text 
a- append data in the end of file
x - create's new file.
'''
# File Object = Open Function ( File Name , Mode)
f=open("stuff.txt","r")
print(f.read(500))

print(f.read(9))

print(f.read(10))

f.close()