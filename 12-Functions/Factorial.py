'''
Escribir una función que reciba un número entero positivo y devuelva su factorial.
'''
from math import factorial
import time

def Myfactorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial (n-1)

def MyfactorialFor(n):
    fac = 1
    for i in range (1 , n+1):
        fac = fac*i
    return fac    
    
facto = int(input("Factorial de: "))
t1 = time.perf_counter_ns()
myFactor = Myfactorial(facto)
t2 = time.perf_counter_ns()
totalTime = t2-t1
print ("My factorial de {} es {}: y tomó: {}".format(facto, myFactor, totalTime))
t1 = time.perf_counter_ns()
myFactor = MyfactorialFor(facto)
t2 = time.perf_counter_ns()
totalTime = t2-t1
print ("My factorial usando FOR {} es {}: y tomó: {}".format(facto, myFactor, totalTime))


t1 = time.perf_counter_ns()
myFactor = Myfactorial(facto)
t2 = time.perf_counter_ns()
totalTime = t2-t1
pyFacto = factorial(facto)
print ("My factorial de {} es {}: y tomó: {}".format(facto, pyFacto, totalTime))


