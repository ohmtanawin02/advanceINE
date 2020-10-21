import math
a = float(input("Enter long     a : "))
b = float(input("Enter long     b : "))
D = float(input("Enter : "))
C = D*math.pi/180
C = math.sqrt(a**2+b**2-2*a*b*math.cos(C))
print("Lenght of side C = ",C)
