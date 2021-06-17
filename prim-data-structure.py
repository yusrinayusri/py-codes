# primitive data structures in python

# List[] (stores data in sequential manner)
myList = []
print(myList)
myList.append([275, 'Gem'])
print(myList)
myList.insert(0, 'Hello World!')
print(myList)
myList.extend([287575, 1])
print(myList)

del myList[2]
print(myList)
myList.remove('Hello World!')
print(myList)
a = myList.pop(0)
print(a)
myList.clear()
print(myList)

myList = [0, 5, 76235, 'hi there', 832, 'hmm']
print(myList[2])
print(myList[0:3])
print(myList[::-1])

print(len(myList))
print(myList.index('hi there'))
print(myList.count(832))
myList2 = [2, 7, 5, 987, 343, 29]
print(sorted(myList2))
myList2.sort(reverse=True)
print(myList2)

# Dictionary{} (stores key:value pairs)
dict = {1: 'Hello', 2: 'World', 3: '890'}
print(dict)

dict[2] = 'There'
print(dict)
dict[3] = 'Hehehehehe'
dict[4] = 'Hmmm'
dict[5] = 'Nam Do San'
print(dict)

a = dict.pop(2)
print(a)
b = dict.popitem()
print(b)
print(dict)
dict.clear()
print(dict)

dict = {1: 'Bobby', 2: 'Nam Do San', 3: 'Park Sae Ro-Yi'}
print(dict[1])
print(dict.get(2))

print(dict.keys())
print(dict.values())
print(dict.items())

# Tuple() (non-modifiable items)
tup = (1, 567, 'Key', 'Antique')
print(tup)

print(tup[2])
print(tup[0:2])
print(tup[:-1])

for x in tup:
    print(x)

tup = tup + (999, 'Hola', 'Bobby')
print(tup)

print(len(tup))
print(tup.index(999))
print(tup.count('Bobby'))

# Sets{} (a collection of unique elements)
sets = {1, 2, 3, 77, 8, 5, 5, 6, 4}
print(sets)

sets.add(788)
print(sets)

sets2 = {2, 5, 6, 788, 45, 6, 3, 3, 4, 0}
print(sets.union(sets2))
print(sets | sets2)
print(sets.intersection(sets2))
print(sets & sets2)
print(sets.difference(sets2))
print(sets - sets2)
print(sets.symmetric_difference(sets2))
print(sets ^ sets2)

