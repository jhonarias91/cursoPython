list1 = ["One", "Two", 'Three']
tuple1 = "January", "February", "march"
set1 = {1,2,3,4}
dictionary1 = {"1": 8, "2": 7, "3":6}
print(type(set1))
for i in list1:
    print (i)

for i in tuple1:
    print (i)    

for i in set1:
    print (i)      

for i in dictionary1.values():
    print (i)      

###Function Range
for i in range(1, 4):
    if (i == 2):
        continue
    if i == 3:
        break
    print (i)
#Steps of 3    
for i in range(1, 10, 3):
    print (i)    
#Negatives   
for i in range(-10, -1, 2):
    print (i)  