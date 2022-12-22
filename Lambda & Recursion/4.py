# 4. Write a recursive python function to print first N odd natural numbers in reverse order


def eve(n):
    if n>0:
        print(n*2-1)
        eve(n-1)

eve(4)