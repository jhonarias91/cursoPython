'''
Ejercicio 1
Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla
'''
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
for i in months:
    month = int(input("Enter the month number: "));
    month-=1
    print (months[month])
