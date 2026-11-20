
# Input and Output in python 
# input means taking data from the user, and output means displaying information to the user.

# we use print to display text to user 
# we can show the text and show text from the variable

name = "Garv"
age = 22

print("Hello from " , name , "and my age is " , age)

# show the values with the help of sep ( separator )

print(name , age , sep = " - ")

# show at the end of the something we use the end=""

print(name, end=" ")
print(age)

# input - input is used to take the input from the user.. 

stu_name = input("Enter the student name: ")
print(stu_name)

# input always return the string for specifiv value we have to use the Type casting

# An f-string lets you insert variables directly into a string using {}.

print(f"Hello my name is {name} and my age is {age}")