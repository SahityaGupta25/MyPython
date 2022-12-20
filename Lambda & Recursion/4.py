# 4. Create a generator to produce squares of first N natural numbers


def sq(n):
    i=1
    while n:
        yield i**2
        i+=1
        n-=1

for x in sq(int(input("Enter a Number\t"))):
    print(x,end=' ')