# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

class Student:

    # Class variable

    class_year = 2024 #Graduating year
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1


print(Student.num_students) # 0 because we haven´t created any students yet

student1 = Student("Alice", 20)
student2 = Student("Bob", 21)
student3 = Student("Charlie", 22)
student4 = Student("David", 23)


print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)
print(Student.class_year) #it´s a good practice to access class variables using the class name, it´s more explicit


print(Student.num_students) #Class variables are shared among all instances of a class

print(f"My graduating class of {Student.class_year} has {Student.num_students} students.") 



