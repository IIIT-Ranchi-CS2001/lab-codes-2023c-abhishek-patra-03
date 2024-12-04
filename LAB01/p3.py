import math
z1 = complex(input("Enter the first impedance : "))
z2 = complex(input("Enter the second impedance : "))
zeq = (z1*z2)/(z1+z2)
print("The equivalent impedance is : ",zeq.real," + j",zeq.imag)