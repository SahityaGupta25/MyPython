'''
# 12. Write a python script to accept one complex number from the user and display the greater number between real part and imaginary part

x=complex(input("Enter a Complex Number\t"))
if (x.real>x.imag):
    print("Real is Greater")
else:
    print("Imaginary is Greater")

'''
# Answer in one line



x=complex(input("Enter a Complex Number\n"))
print(x.real if x.real > x.imag else x.imag  )