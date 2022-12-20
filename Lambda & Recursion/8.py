# 8. Create an endless iterator using generator method to produce Square numbers


def sq():
    i=1
    while True:
        yield i**2
        i+=1
        
it=sq()


l1=[]
while True:
    ans=input("Choose between 'y' & 'n'\t")
    if ans=='y':
        x=next(it)
        print(x)
        y=l1.append(x)
    elif ans=='n':
        print(l1)
        break


