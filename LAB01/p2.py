import math
a = int(input("Enter the first side of the triangle : "))
b = int(input("Enter the second side of the triangle : "))
c = int(input("Enter the third side of the triangle : "))
s=(a+b+c)/2
print("Area of the given triangle is : ",math.sqrt((s*(s-a)*(s-b)*(s-c))))
print("Perimeter of the given triangle is : ",(a+b+c))
a1 = math.acos((a*a+b*b-c*c)/(2*a*b)) * (180/math.pi)
a2 = math.acos((a*a+c*c-b*b)/(2*a*c)) * (180/math.pi)
a3 = math.acos((b*b+c*c-a*a)/(2*b*c)) * (180/math.pi)
print("The three angles of the triangle are : ",a1,", ",a2,", ",a3)