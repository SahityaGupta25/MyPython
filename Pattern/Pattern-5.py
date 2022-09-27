'''
 Write a Program to Print Pattern Like this
 
 * * * *
   * * *
     * *
       *

 '''
for i in range(1,5):
    for j in range(1,5):
        if (j>=i):
            print("*",end=' ')
        else :
            print(' ',end=' ')
    print()
    