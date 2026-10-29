# unlike the Nodejs the python is not single thread is not single thread to run that 
# The threading Library in the python is used to handle the multiple Tasks or run the multiple tasks in the Same Library
# It allows the User to turn this Tasks into the separate light weight tasks like call Threads 

# Lets see a example of the Threading 
import threading
import time

def printName(name):
    time.sleep(2) # sleep the current thread by the 2 seconds
    print("name:" , name)

t1 = threading.Thread(
    target=printName,
    args=("Task 1",)
)

t2 = threading.Thread(
    target=printName,
    args=("Task 2",)
)

t1.start()
t2.start()

# they both will came with the same time