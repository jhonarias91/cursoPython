cadena = "este es un ejemplo de substring (debanado de cadenas). este otro"

'''
print(len(cadena))
print (cadena[0: 2])
print (cadena[: 2])
print (cadena[20: ])
print (cadena[: ])
print (cadena[-1])#Starts from the end

print (cadena.capitalize())
print (cadena.title())
print (cadena.swapcase())
print (cadena.upper())
'''
first3 = cadena[0:3]
first3_2 = cadena[:3]
print (first3)  
print (first3_2)
from3 = cadena[3:]
print (from3)
last3 = cadena[-3:]
print ("Last 3 negative: "+last3)
print ("cadena[-3]: "+cadena[-3])
#Get the last 3 letters witout using negative

last3 = cadena[len(cadena)-3:]
print ("Last 3 using len(): " +last3)