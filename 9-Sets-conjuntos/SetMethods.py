#Set is like a list, but not repeated values
set1 = {1,2,3,4,5}

set1.add(7)
#both deletes
set1.remove(3)
set1.discard(3)
print(set1)
#pop deletes and arbitrary element
randomElement = set1.pop()
print(randomElement)

#add iterables elements
set1.update([5,6,8])
print(set1)

#let the set empty
set1.clear()