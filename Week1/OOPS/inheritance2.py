# If we define one method into Base class and the Second Method into the Derived class and then Creating the Obejct of 1st one which is the Base class then to use the Super keword to access

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

student = Student("Garv", "thakral")

print(student.name)
print(student.course)