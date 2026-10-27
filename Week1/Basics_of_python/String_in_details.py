# Python String 
# String is the collection of the Characters or we can say that the String is the collecttion of the sequences of the Characterts 

name = "Garv"
city = "Ambala"
state = "Tamil Nadu"

# Let's print this 
print(name);
print(city);
print(state);

# There is Many different Way to Write the Python Mainly three 

type1 = "Python"
type2 = 'Python'
type3 = """Python
is Excellent"""

# We can Use the Both the Double Quotes and the SIngle Quotes 
# Strings containing quotes

message = "I'm Learning Python"  # we can use the Single Quotataion inside the Double Quotation 

print(message);

# we can also insert the slash here '\' into the string
message1 = "I\'m Learnng python once again"

print(message1);

## Python is the Immutable we cannot change after the Creation of the Variable 

# message1[0] = 'H' 
# print(message1) # TypeError: 'str' object does not support item assignment

# Instead we can create the new Variable and then we can store the variable 

name = 'Aman'
name = 'D' + name[1:]

print("The new name created after the string Immutablity we created new one:" , name); #Dman

