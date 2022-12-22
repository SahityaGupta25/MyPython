# 5. Write a recursive python function to print first N even natural numbers.

def eve(n):
    if n>0:
        eve(n-1)
        print(n*2)

eve(4)
