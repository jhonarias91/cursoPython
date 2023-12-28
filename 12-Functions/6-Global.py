def setGlobalVar():
    global num1, num2
    num1=100
    num2=80
    return num1+num2

setGlobalVar()

result = num1-num2
print (result)