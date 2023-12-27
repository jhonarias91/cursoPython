dict = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

for i in range (1,100):
    pais = input("Ingrese un pais:")
    if (pais.lower() == "exit"):
        break
    pais = pais.title()
    capital=dict.get(pais)  
    isPresent = capital in dict  
    if (capital == None):
        capital= input("No lo se, cual es?: ")
        dict[pais] = capital.capitalize()
        print ("Ok, la capital de {} es: {}".format(pais, dict[pais]))
    else:
        print ("La capital de {} es: {}".format(pais, capital))
