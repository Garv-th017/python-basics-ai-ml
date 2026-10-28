# In python How we can create a Function ??
# Function is the resuable peice of the code that is used in the overall project we can use and we can create once and where is the same logic use we can call and then use that same one ... 

# syntax to create the Function in the python 
# python use a def keyword to define the function that we can use for example the Basic of the python 

def print_hello():
    print("Hello Python ! how are you")

print_hello()  # we can call the python using the function_name()


number1 = int(input("What is the Number 1 Value :"))
number2 = int(input("What is the Number 2 Value :"))

def sum_of_two_val(num1,num2):
    sum = num1 + num2
    return sum

print("Value of the two number is :" , sum_of_two_val(number1,number2))

# The fucntion has also the same rules that the Variable has not the same they have the different - They have the also the same rules of the variables 

# We can use 'return' keyword to return the something from the function and use into the code. 

# and fucntion definition is never empty and we can use the 'pass' if we want to use the skip one 

# *args and **kwargs and we didn't know how much arguement we have to pass in advanced so we can use the 

# *args - is used to accept any number of positional arguement in the function 

def numbers(*nums):
    print(nums)

numbers(1,22,1,1,1,1,1)

# **kwargs - From the Name we are getting the it's the keyword arguements from the name getting that it accepts the keyword arguement how much we have to pass 

def names(**data):
    print(data)

names(name = "Garv" , age = 11 , Study = "MSC")

# Main difference between in that the *args that the *args collect the value in the form of tuples and the kwargs - in the form of the dictonaries key value 


# Decorator - In python the Decorator is the function that add the exttra functionality to another functions without changing the exsisting functionality

def my_decorator(func):
    def wrapper():
        print("Function started")
        func()
        print("Function ended")
    return wrapper


def greet():
    print("Hello, Garv!")


greet = my_decorator(greet)

greet()

# Lambda Function - Lambda function is the function that is the anonymous and we can use it in the short term
# Lambda : Arguements : Expression

x = lambda a : a +1
print(x(2)) # we pass arguement here 

# The Recursion is the process where the function calls itself

# Generator is useful when you want to process the Large amount of data and not to save intot he Memeory the generator function return the value at a time 

def get_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

numbers = get_numbers()

print(numbers)


# It returns the <generator object get_numbers at 0x0000027B0EDF8BF0> and Basically it's not the value 

# To Getting the value we have to iterate over that 

for i in numbers:
    print(i)
    i+=1

#yield keyword is the main part of genertor it basically return a value and stop working and when the generator the next values comes it runs else not 