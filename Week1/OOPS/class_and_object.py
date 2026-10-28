# we can create a class using the Keyword 'class'
class myclass:
    x = 5

print(myclass) # it print the class 

# creating object into the python class 

obj1 = myclass()
print(obj1.x)

# The init method in the python : __init__() this method is always executed when the Class is created.
# this method is used to self assigned the Object values 

class student_info():
    def __init__(self,name,age):
        self.name = name
        self.age = age

Obj2 = student_info("Garv" , 21)

print(Obj2.name);

# during init calling we can also give the default values __init__(name="Garv" , age = 11) values

# The 'self' Parameter - Self Parameter is the reference to the current instance of the object 
# like the 'this' keyword in the other programming Languages 

# Magic Methods - Magic Methods are the Methods that are from the start and end with the double score __ and end with also __ and they also called the dunder methods (double underscore). But we use it calles the dunder method 

# LIke the 
# __init__()
# __str__()
# __len__()
# __add__()

# This method is the built in method of the Classes that is help and we can use 'self' keywords to working with them and they help to working with them 

