# 12. Write a python script to accept one complex number from the user and display the greater number between real part and imaginary part

x=complex(input("Enter a Complex Number\t"))
if (x.real>x.imag):
    print("Real is Greater")
else:
    print("Imaginary is Greater")
