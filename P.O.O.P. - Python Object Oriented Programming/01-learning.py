from car import Car

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)


#Methods are actions that objects can perform. They are defined in the class definition.

car1.drive()
car2.drive()
car3.stop()

car1.describe()
car3.describe()