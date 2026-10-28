# In python How we can create a Function ??
# Function is the resuable peice of the code that is used in the overall project we can use and we can create once and where is the same logic use we can call and then use that same one ... 

# syntax to create the Function in the python 
# python use a def keyword to define the function that we can use for example the Basic of the python 

def print_hello():
    print("Hello Python ! how are you")

print_hello()  # we can call the python using the function_name()


number1 = int(input("What is the Number 1 Value"))
number2 = int(input("What is the Number 2 Value"))

def sum_of_two_val(num1,num2):
    sum = num1 + num2
    return sum

print("Value of the two number is" , sum_of_two_val(number1,number2))
