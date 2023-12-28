from math import sqrt
def fibo (n):
    if n == 0:
        return 0
    if n==1:
        return 1
    return  fibo(n-1) + fibo(n-2)

#print (fibo(6))

def isPrime(n):
    if (n < 2):
        return False
    root = int(sqrt(n))
    for i in range(2, root):
        if (n % i == 0):
            return False
    return True

n = int(input ("Ingrese un número para verificar si es primo: "))

print("{} es primo? {}".format(n, isPrime(n)))

