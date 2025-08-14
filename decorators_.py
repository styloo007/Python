# The Real Use Case of Decorators Are Logging, Caching and Authentication

import time
from datetime import datetime 

# def decorator_(func):
#     def wrapper():
        
#         print("Before the function runs")
#         func()
#         print("After the Function runs")
        
#     return wrapper



# @decorator_
# def say_hello():
#     print("Hello")


# say_hello()


# Example 2

def timer(func):
    func()
    def display_time():
        print("Printing Local Time")
        print(datetime.now())
        print("Sleeing for 5 secs")
        print(time.sleep(5))
        print("Printing Local Time")
        print(datetime.now())
    return display_time

@timer
def activateTimer():
    print("Activating The Functions: \n")

activateTimer()