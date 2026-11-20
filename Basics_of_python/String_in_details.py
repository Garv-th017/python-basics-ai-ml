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

# string Indexing - String Indexing means accessing a string Character with the Help of the Index 

# There are Two types of Indexing Has - Positive Indexing and Negative Indexing 

# Postive Indexing Like from ( 0 to Ongoing )
# Negative Indexing Like from the ( -1 to the Last we have i.e. -10)

# Here Indexing starts from the 0 

# And also the Characters Stores in the Memory they took some bytes 

Student_name = "Roshni"
print(Student_name[0]); # R
print(Student_name[1]); # o
print(Student_name[2]); # s
print(Student_name[3]); # h

# And Also we can Access from the Negative Also 

print(Student_name[-1]); # i - Basically Negative side 

# String Sliing - From the Name we are getting the SLicing - Slicing means extracting the Part of the string 

# And we can Give the Start and end index with the Help of we can access our String Partion 


# Basic Indexing is this one String[start : end ]

new_name = "Garv"
print(new_name[0:1]);