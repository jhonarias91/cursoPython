list=[20, 50, "Curso", 'Python', 3.14]
print (list)
#list[1] = input("Ingrese un dato: ")
#list[0] = input("Ingrese otro dato: ")
#print(list)

numbers=[]
for i in range(1,11):
    numbers.append(i)
numbers[4] *= 2
numbers[7] *= 2
numbers[9] = numbers[9]*2
print (numbers)