#dictionary is a collection of key-value pairs. Ordered and changeable. No duplicate keys allowed.

capitals = {'USA':'Washington DC', 
            'India':'New Delhi', 
            'China':'Beijing', 
            'UK':'London',
            'Brazil':'Brasilia'}

#print(dir(capitals))

#print(help(capitals))
print(capitals.get('Japan'))

if capitals.get('Japan') == None:
    print('That capital existis')
else:
    print("That capital doesn't exist")

if capitals.get('Brazil') == None:
    print('That capital existis')
else:
    print("That capital doesn't exist")

capitals.update({'Germany':'Berlin'})

print(capitals)

capitals.update({'Germany':'Bonn'})
print(capitals)

capitals.pop('Germany')
capitals.popitem()

#capitals.clear() #clears the dictionary
print(capitals)

keys = capitals.keys()
print(keys)

for key in capitals.keys():
    print(key)

values = capitals.values()
print(values)

for value in capitals.values():
    print(value)

items = capitals.items()
print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")