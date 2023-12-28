'''
Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista. Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas
'''
numbers = []
def askNumbers():
    a = int(input("Cuantos números desea agregar: "))
    i=1
    while i <= a:
        n = int(input("Ingrese el número {}: ".format(i)))
        numbers.append(n)
        i+=1

askNumbers()
def showEvenAndOdds():
    even, odds = [], []
    for i in numbers:
        if (i % 2 == 0):
            even.append(i)
        else:
            odds.append(i) 
    print(even)           
    print(odds)      
         
showEvenAndOdds()

