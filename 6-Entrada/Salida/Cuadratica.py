import math
from math import sqrt

a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

result1 = (-b + math.sqrt(b**2-4*a*c))/(2*a)
print("Result 1: ",result1)

if (a>0):
    result2 = (-b - math.sqrt(b**2-4*a*c))/(2*a)
    print ("Result 2: ",result2)