a = input ("Ingrese a: ")
b = input ("Ingrese b: ")


if len(a) >= 3 and len(b) >= 3:
        lastA = a[-3:]
        lastB = b[len(b)-3:len(b)]
        if (lastA == lastB):
            print ("Riman")
        elif a[-2:] == b[len(b)-2:]:            
            print ("Medio Riman")
        else:
            print ("No Riman")
