i = 0
while i < 10:
    print (i) 
    i+=1

tabla = int(input("Ingrese la tabla: "))    
i=0
result=0
while i < 10:
    i+=1
    result=tabla*i
    print ("{} x {} = : {}".format(tabla,i,tabla*i))