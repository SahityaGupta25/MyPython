# 1. Write a recursive python function to print first N natural numbers.

def Nnatural(n):
    if n>0:
        Nnatural(n-1)
        print(n)

Nnatural(5)