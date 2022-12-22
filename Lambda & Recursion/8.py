# 8. Write a recursive python function to print cubes of first N natural numbers

def cb(n):
    if n>0:
        cb(n-1)
        print(n**3)

cb(4)