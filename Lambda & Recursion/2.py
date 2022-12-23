# 2. Write a recursive python function to print first N natural numbers in reverse order


def Nnatural(n):
    if n>0:
        print(n)
        Nnatural(n-1)

Nnatural(5)