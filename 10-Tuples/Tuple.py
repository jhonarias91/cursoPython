tuple = (1,2,3,4,5)
tuple2= 1,2,3,4,5

print (tuple == tuple2)

#same as list
one= tuple[0]
#return a new tuple
deban= tuple[:2]
print(deban)
#from pos 3 to end
deban= tuple[3:]
print(deban)
#When negatives, it go the last 3
last3= tuple[-3:]
print(last3)
#All elements but not last 2
excludeLast2= tuple[:-2]
print(excludeLast2)

#concat tuples
print(tuple+tuple2)