# 3. Write a python script to calculate sum of cubes of first N natural numbers
# ==============================================================================

n=int(input("Enter a Number\t"))
cb=0
for a in range(1,n+1):
    cb=a**3+cb
print("Sum of cubes of first ",n, "natural numbers is",cb)