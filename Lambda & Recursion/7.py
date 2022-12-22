# 7. Write a recursive python function to print squares of first N natural numbers


def sq(n):
    if n>0:
        sq(n-1)
        print(n**2)

sq(14)