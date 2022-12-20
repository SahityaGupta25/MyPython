# Accessing Each Element of a Container using While Loop.

t1=(16, 25, 2, 9, 66, 29)
it=iter(t1)
while True:
    print(next(it),end=' ')
print(type(it))

