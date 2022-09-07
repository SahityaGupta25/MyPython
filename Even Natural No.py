# Write a Python Program to print First N Even Natural Numbers
# -------------------------------------------------------------


N=int(input("Enter a No.\n"))
i=2
while (i<=N and i%2==0):
    print(i,end=' ')
    i+=2