dict = {1:2, 2:3, 3:4}

#Pop get and delete by key
a = dict.pop(3)
print (a)
print (dict[2])

#clear remove all data
dict.clear()

#get(1) similar to [1]
print(dict.get(1))

#setDefault(), similar to dict['key']='value'
dict.setdefault(4, 5)
print(dict)

#mix 2 dictionaries in one
dict2 = {3:5, 5:7}
dict.update(dict2)
print(dict)

#Create a copy
dict.copy()