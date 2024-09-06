#map(function, collection) - Applies a given function to all the items in an collection and returns a new collection

def c_to_f(temp):
    return ((9/5) * temp) + 32

celsius_temps = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0]

fahrenheits_temps = map(c_to_f, celsius_temps)


print(celsius_temps)

for temp in fahrenheits_temps:
    print(temp)

# if you want a list, enclose the map function in a list function
fahrenheits_temps2 = list(map(c_to_f, celsius_temps))

print(fahrenheits_temps2)

#we could use a lambda function instead of a normal function

fahrenheits_temps3 = list(map(lambda temp: ((9/5) * temp) + 32, celsius_temps))

print(fahrenheits_temps3)