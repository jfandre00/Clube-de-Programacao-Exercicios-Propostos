#Allows a class to inherit attributes and methods from another class
#Helps with code reusability and extensibility
# class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")
    

class Dog(Animal):
    def speak(self):
        print(f"{self.name} is barking")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} is meowing")

class Mouse(Animal):
    def speak(self):
        print(f"{self.name} is squeaking")

dog = Dog("Bento")
cat = Cat("Chaninha")
mouse = Mouse("Mickey")


print(dog.name)
dog.eat()
print(dog.is_alive)

cat.sleep()

mouse.eat()

dog.speak()
cat.speak()
mouse.speak()
