# 3. Create a generator to produce first n even natural numbers

def odd(n):
    i=2
    while n:
        yield i
        i+=2
        n-=1

for x in odd(int(input("Enter a Number\t"))):
    print(x,end=' ')