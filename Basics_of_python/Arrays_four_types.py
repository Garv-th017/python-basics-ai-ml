# Arrays has the Four Types that is in the python we have 
# List , Tuples , Set and Dictionary 

# List - It's syntax is the [] and here in the Syntax 
# List is ordered and we can change and is mutuable after the creation

List = ["Garv" , "Aman" , "Rahul"];

List[0] = "Naman" # We can change this one 
print(List) 

# Tuples - Tuples Here is the Meaning we can't change after the creation like there format is the () and we can change after the creation and is the ordered one 

# The example is the for the tuples is 

tuples = ("List" , "mango" , "Apple")
print(tuples) # original List

# tuples[0] = "Dictoniary"  # It gives error (TypeError: 'tuple' object does not support item assignment)
# print(tuples) # Is we can modify this No we can't modify 

# Sets :- Sets Basically is the ordered collection of the items and it removes the Duplicates Items by default and also make this one Better 
# Syntax is ({})

Is_even_numbers = {1,2,1,1,3,2,4,5,10}
print(Is_even_numbers); # it's makes only shows the Real Numbers not the Duplicate One's

# {1, 2, 3, 4, 5, 10} - This is the Unique items 

# Dictionary ({key: value}) : Dictionary Is the Key values pairs and this can be stores the key value pairs 

# we can do like this one :- 
Student_Details = {
    "Name" : "Garv",
    "age" : 21,
    "ph_no" : "123123131"
}

# We can also update the Dictonary
print(Student_Details["Name"]) # that prints the value we can access the variables from this
print(Student_Details["age"]) # It prints the Age basically
print(Student_Details["ph_no"])

# changing the value is the mutuable ??
Student_Details["age"] = 31 # It updates the age 

print(Student_Details)