# 3. Write a recursive python function to print first N odd natural numbers

def eve(n):
    if n>0:
        eve(n-1)
        print(n*2-1)

eve(4)