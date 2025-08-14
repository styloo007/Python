# Print 1 to 10

# for i in range(1,11):
#     print(i)







# 3 Table using the while loop

# a = 3
# b = 1

# while b!=11:
#     print(a*b)
#     b = b+1





# Square of a number using function

# def squareOfANumber(num):
#     return num*num


# print(squareOfANumber(5))





# Collections in Python (Lists, Tuples, Set, Dict )

# List - Ordered, Mutable, and Allows Duplicates
# Set - Unordered, Mutable and No Duplicates
# Tuple - Ordered, Ummutable and Allows Duplicates
# Dict - Ordered, Mutable and No Duplicates


#Lists 
# fruits = ["Apple","Mango","Banana"]
# fruits.append("Strawberry")
# print(fruits[0])
# fruits[0] = "Litchi"

# #Tuple
# coordinates = (4,5)
# print(coordinates[1])
# coordinates[0] = 5

# #Set
# fruits_set = ["Apple", "Mango", "Apple", "Banana"]
# fruits_set.append("Orange")
# print(fruits_set[0])


# #Dict
# maps = {
#     "name":"Shashank",
#     "age":20,
#     "gender":"male"
# }
# print(maps)
# print(maps["name"])
# maps["age"]=22


# #String Manipulation

# text = "Hello World in py"
# print(text.lower())
# print(text.upper())
# print(text[0])
# print(len(text))

# text2 = "from Shashank"
# print(text+text2)

# text3 = "Agasimani"
# print(f"{text}+{text2}+{text3}")

# print(text.strip())
# print(text.replace("Hello", "Hey"))
# print("Hello" in text)  # Returns true else False

# sentence = "Learn Python Programming"
# words = sentence.split()
# print(words)
# joined_words = "-".join(words)


# #File Handling in Python

# #Reading the complete file
# with open("sample.txt","r") as file:
#     content = file.read()
#     print(content)
    
# #Reading the file line by line
# with open("sample.txt", "r") as file:
#     for line in file:
#         print(line.strip())
        
# #Writing into a file
# with open("sample.txt","w") as file:
#     file.write("Hey, this is Shashank")
    
# #Appending text into an existing file
# with open("sample.txt",'a') as file:
#     file.write("\n This new line is append via py")
    
    
    
#OOP in Python

#OOP helps reorganise code using classes and objects, making it more reusable and logical    
# Class is a blueprint
# Object is instance of a class


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
        
#     def greet(self):
#         print(f"Hey there I'm {self.name} and I'm {self.age} years old")
        
        
# person1 = Person("Shashank", 22)
# person1.greet()


# # The  __init__ runs automatically when an object is created and is used to initialize the attributes

# class Calculator:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
        
#     def add(self):
#         return self.num1 + self.num2
    
#     def sub(self):
#         return self.num1 - self.num2
    
#     def mult(self):
#         return self.num1 - self.num2
    
#     def divide(self):
#         return self.num1 / self.num2


# cal1 = Calculator(10, 5)
# print(cal1.add())
# print(cal1.sub())
# print(cal1.mult())
# print(cal1.divide())


# # Class with Default values
# class Dog:
#     def __init__(self, name="Tom", breed="Lab"):
#         self.name = name
#         self.breed = breed
#     def greet(self):
#         print(f"{self.name} Says Woof!")
    
# dog1 = Dog()
# dog1.greet()

# dog2 = Dog("Jim","Husky")
# dog2.greet()

# class Car:
#     def __init__(self, brand, color, model, year):
#         self.brand = brand
#         self.color = color
#         self.model = model
#         self.year = year
    
#     def display_specs(self):
#         print(f"The Car Details are as follows:\n Brand:{self.brand}\n Color:{self.color} \n Model:{self.model}\n Year:{self.year}")
        

# car1 = Car("Porshce","Red","GT3RS","2012")
# car1.display_specs()


# #Exception Handling
# try:
#     x = 100/0
# except ZeroDivisionError:
#     print("You cant divide a number by zero")
    
    
# try:
#     num = int(input("Enter a number to divide with: "))
#     div = 100/num
#     print(div)
# except Exception as e:
#     print(f"An Error Occured: {e}")
    

#Using Else and Finally

try:
    num1 = int(input("Enter Number1: "))
    num2 = int(input("Enter Number2: "))
    ans = num1/num2
except Exception as e:
    print(f"An Error Occured: {e}")
else:
    print(f"This is the answer: {ans}")
finally:
    print("Doesnt matter if there's an exception or not, This always runs")
    
    
# Modules and Packages

# A Module is nothing but a python file .py with a lot of functions, classes variables etc. That can be used in another file

import math_utils

addTwo = math_utils.add(71, 5)
print(addTwo)

subTwo = math_utils.subtract(75, 5)
print(subTwo)


# A Package is a folder with collection of modules and an __init__ file, could be empty as well. Helps when grouping related code is needed



from sample_package import math_utils, string_utils

print(math_utils.add(1,2))
print(string_utils.shout("hey shashank"))