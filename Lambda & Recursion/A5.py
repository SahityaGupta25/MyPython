# Write a Recursive Function to calculate sum Squares of N natural Numbers
def sqs(n):
    if n==1:
        return 1
    a=n*n+sqs(n-1)
    return a

s=sqs(3)
print(s)