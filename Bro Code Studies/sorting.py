#sorting in python .sort() and sorted() functions
# lists, tuples, dictionaries, objetcs

fruits = ['grape', 'raspberry', 'apple', 'banana']
numbers = [2, 3, 1, 4]
fruits.sort()
print(fruits)
numbers.sort(reverse=True)
print(numbers)

frutas_tupla = ('grape', 'raspberry', 'apple', 'banana')

#.sort method does not work with tuples, because it is immutable

print(sorted(frutas_tupla))
sorted_fruits = tuple(sorted(fruits, reverse=True))
print(sorted_fruits)

#sorting dictionaries

d = {'banana': 105, 'apple': 72, 'coconut': 354, 'orange': 73}

frutas_calorias = dict(sorted(d.items()))
print(d)
print(frutas_calorias)

#sort by key
frutas_calorias2 = dict(sorted(d.items(), key=lambda item: item[0], reverse=True))
print(frutas_calorias2)


#sort by value
frutas_calorias3 = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
print(frutas_calorias3)


#Objects

class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __repr__(self):
        return f'Fruit({self.name}, {self.calories})'

fruits = [Fruit('grape', 100), 
          Fruit('raspberry', 200), 
          Fruit('apple', 300), 
          Fruit('banana', 400),
          Fruit('orange', 50)]

fruits = sorted(fruits, key=lambda fruit: fruit.name) 
print(fruits)

fruits_reverse = sorted(fruits, key=lambda fruit: fruit.name, reverse=True)
print(fruits_reverse)

fruits_calories = sorted(fruits, key=lambda fruit: fruit.calories)
print(fruits_calories)