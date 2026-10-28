# In python the Operator is used to Perform Some Operations
# There are DIfferent Types of the Operators are Present :-
# Arithmetic Operators
# Assignment Operator
# Logical Operator
# Comparison Operators 
# Identity Operators 
# Membershp Operators
# Bitwise operators


# Each Operators perform some operations On the variables

# Let's Perform Some Operations

x = 51
y = 2

print(x+y) # Addition
print(x-y) # Subtraction
print(x*y) # Multiplications
print(x/y) # Division - Return the Quotent in the Float 
print(x%y)  # Modules 
print(x**y) # Exponental 
print(x//y) #Floor Division - Return The Quotent in the Whole Number

# In python the Division is the Two We used 
# / - Division Return the Float Actual
# // - Division Floor that return the Nearest Value

# Assignment Operators - Assignment Operators are used to Assign Values 
# Basically they have some Short way Let's Check here
# Some examples are here 

# = , += , -= , *= and many more 

# A new operator comes that is in the python 3.8 that is the Warlus Operators ':=' 

# The Walrus Operator (:=) in Python allows you to assign a value to a variable and use that variable in the same expression.

# Let's Understand the DIfference between the = and the :=

name = "Garv"

if (len(name) > 0):
    print(name)

# This is the Oldest way to use the python now in this First i have to Assign the name and then i have to use that but here In the Warlus Operators is not Like that 

if (name := "garv thakral"):
    print(name)

# Ternary Operator is used to Make the Short Form of the IF ELSE 

Age = 18

if(Age > 18):
    print("You are Elgilable for vote")
else: 
    print("You are not Elgilable for the voting")

# We can write this into the Sort Form Like 
age = int(input("Please Enter your age :"))

message = "Adult" if age >=18 else "Minor"
print(message)

# Comparison Operators :- Comparison Operators is used to add to Compare the two values 

# There are different Types of Operators are present
# == , != , > , < , >= , <= and many more

