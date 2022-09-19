'''
Write a Program using For Loop take Input from user . If there is 'r' present in thaht input string print string till 'r' . If there is no 'r' in the string print it as well as print "All Characters are Processed".
-----------------------------------------------------------------------------------------------
'''

x=input("Enter a String\t")
for y in x:
    if (y=="r"):
        break
    print(y,end=' ')
else:
    print("All Characters are Processed")
