# The if , else if and the others they are the statements 
# Condition Statement are used to run the statement based on the some conditions - Like (if something is fulfil then run this else not)

# If statement - If is used to Run when there is something we have to run means if the condition passed then run the statement else nothing see the example

elgilable_age = int(input("Enter the age value"))
if(elgilable_age > 18 and elgilable_age < 56):
    print("sir you are elgilable for the Voting ")


# Elif - Elif keyword is the keyword that is used to Run the Condition in the case if the 'if' condition is not satisfy 

if(elgilable_age > 18 and elgilable_age < 56):
    print("sir you are elgilable for the Voting But check you have voter card")
elif(elgilable_age > 17 and elgilable_age < 56):
    print("Next year you are elgilable")
else: 
    print("Not you are not elgilable")

# you can also use the shortend if statement - in the one line 
# Python also provide the Nested if Statement 


# if(elgilable_age > 18 and elgilable_age < 56):
#     print("sir you are elgilable for the Voting But check you have voter card")
#     if(elgilable_age > 56 and elgilable_age < 70):
#         print("Is Reall you want to give the Vote , IF yes you may , Take care Health")
#         if(elgilable_age > 70 and elgilable_age < 90):
#             print("Wait we have to confirm with your family , You can give vote easily!")
# else:
#     print("NO Vote!")

# This is the wrong code and example i written let's fix this

if(elgilable_age > 18 ):
    if(elgilable_age < 56):
        print("sir you are elgilable for the Voting But check you have voter card")
    else:
        if(elgilable_age <  70):
            print("Is Reall you want to give the Vote , IF yes you may , Take care Health")
        else :
            if(elgilable_age < 90):
                print("Wait we have to confirm with your family , You can give vote easily!")
else:
    print("NO Vote!")


# Pass - Pass statement is used in python when you haven't implement the code logic yet and only the Pass to the Other block it's not giving error just have to show and usecase 