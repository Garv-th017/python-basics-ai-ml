# Python has many different data types that we can acutally used 
# string , float , numbers , boolean , algebric and many things

name = "Garv" #string
age = 21 #int or numeric
marks = 10.10 #float
isActice = True #boolean

#Tuples is the data type in the python that is used to store the different elements in one vairable. 
# It can't be changed after creation because it's immutable we can't change
# the format of the tuples is ()
student = ('Garv' , 22 , 'KKR')

#List - List is the ordered collection and it can be changed after the creation ( mutuable )
# The format of the List is - []
skills = ["Python", "JavaScript", "React"]

# A set is a collection which is unordered, unchangeable*, and unindexed.
# The format of the set is { }
# But the output contains the uniqu value

numbers = {1,2,3,4,5,6,7,8}

# Dictionary 
# A Dictionary is a collection of the key value pairs that is used to stored the values in the form of the key value pairs 

student1 = {
    "name": "Garv",
    "age": 22,
    "city": "Mohali"
}

# None - None represent the absence of the values 

IsPresent = None

# primitve data types are the built in data types that we can use 

### print the values of the different vairables that stored the different data types

print(name)
print(age)
print(marks)
print(isActice)

print(student)
print(skills[0])
print(numbers)
print(student1["name"])


