# 2. Create a generator to produce first n odd natural numbers

def odd(n):
    i=1
    while n:
        yield i
        i+=2
        n-=1

for x in odd(int(input("Enter a Number\t"))):
    print(x,end=' ')


