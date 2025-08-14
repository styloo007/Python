# Decorators are functions that take another function as an argument and return a modified version of that function

def myDecorator(func):
    def wrapper():
        print("This line would print before the function is called")
        func()
        print("This line would print after the function is called")
    return wrapper

@myDecorator
def sayHello():
    print("The Function is called!")
    

sayHello()


# Decorator with an argument

def myDecorator2(timer):
    def myDecorator3(func):
        def wrapper(*args, **kwargs):
            for i in range(timer):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return myDecorator3
            
@myDecorator2(3)
def greet(name):
    print(f"Hello, {name}")

greet("Styloo")




