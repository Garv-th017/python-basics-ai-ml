# async and await is the necessary When we working with the tasks & Process that took times to complete and depended on other 
# Let's see the example

import time
import asyncio

def func1():
    print('task 1 is done')
    time.sleep(5)   # sleep for the 5 Seconds the process 
    print('task 2 is done')
    print('task 3 is done')

def func2():
    print('task 4 is done')
    print('task 5 is done')

func1()
func2()

# Problem: Task 2 has to wait even though it doesn't need Task 1 to finish. and same as the Other Tasks

# This problem is solved using the Async Programming

# Async Programming - Allow the One tasks to continue there tasks until one tasks is already working on the 1st one. That didn't block the continue to the one until one task is in the process. 

# we can use the async await mean while working with the asynronous programming. 

async def greet():  # creates the Async func
    print('Hello Python you are great !')

async def wait(): # creates the Async func
    await greet() # continue the Coroutine

asyncio.run(wait()) # Start an event Loop to Run the wait() async Function


