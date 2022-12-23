# Sum of N Natural Numbers
def x1(n):
    if n==1:
        return 1
    x=n+x1(n-1)
    return x

s=x1(3)
print(s)