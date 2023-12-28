'''
Escribir una función que reciba un número entero positivo y devuelva su factorial.
'''

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial (n-1)

facto = int(input("Factorial de: "))
print ("El factorial de {} es {}: ".format(facto, factorial(facto)))