# 7. Create an endless iterator using generator method to produce terms of Fibonacci series

def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
it=fib()

l1=[]
while True:
    ans=input("Choose between 'y' & 'n'\t")
    if ans=='y':
        x=next(it)
        print(x)
        y=l1.append(x)
    elif ans=='n':
        print(l1)
        break



