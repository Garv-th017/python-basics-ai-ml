# Inheritance Is the Part of the OOPS concet that allow to inhert all the properties and method of the Parent Class we are Ineting their properties andmethod 
# The parent Class also called the Base class 
# The children class also called the Derived class 

class my_student():
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName

    def printDetails(self):
        print("Here is the FirstName" , self.firstName , "And the Last Name is" , self.lastName)

class my_student_base(my_student):
    pass

stu1 = my_student_base("Garv" , "Thakral")
print(stu1.firstName)
print(stu1.lastName)