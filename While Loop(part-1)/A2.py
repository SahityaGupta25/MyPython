'''
Write a Program to ask user to enter a even no. three times .If user fails to enter a even number all 3 times announce him a loser . If user entered a even no then no more chances will be given to him or her announce he/she winner. 
'''
#------------------------------------------------------------------------------------------

i=1
while (i<=3):
    x=int(input("Enter a Number:\t"))
    if (x%2==0):
        print("Winner")
        break
    i+=1
else :
    print("Loser")