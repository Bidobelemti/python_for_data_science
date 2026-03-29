# Chapter 3 - introduction to Object-Oriented Programming (OOP)
# 3.1 Classes and Objects
# In Python, we can define a class using the class keyword. The syntax for defining a class is as follows:
"""class ClassName:
    # block of code to define the class
    def method_name(self, parameters):
        # block of code to define the method
        return value
"""
# Example:
class Person:
    def __init__(self, name, age):
        self.name = name    # Atribute of the class
        self.age = age      # Atribute of the class

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
# Class is composed of atributes and methods. Atributes are variables, while methods are functions the belong to the class.
# In each class, we can define a constructor method __init__() that is called when an object of the class is created. 
# The __init__() method is used to initialize the attributes of the class. The self parameter is a reference to the current instance of the class and is used
# we could define any constructor method, each one with differents parameters, but the convention is to use __init__() as the constructor method.
# We can create an object of the class by calling the class name followed by parentheses. For example:
person1 = Person("Mauricio", 23)
print(person1.greet()) # Output: Hello, my name is Mauricio and I am 23 years old.

# 3.2 Inheritance
# Inheritance is a fundamental concept in object-oriented programming that allows a new class (called a child class or subclass) to inherit
# attributes and methods from an existing class (called a parent class or superclass). This promotes code reusability and establishes a natural hierarchical relationship between classes.
# In Python, we can define a child class that inherits from a parent class by specifying the parent class in parentheses after the child class name. The syntax for defining a child class is as follows:
"""class ChildClass(ParentClass):
    # block of code to define the child class
    def method_name(self, parameters):
        # block of code to define the method
        return value
"""
class employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age) # this will call the constructor of the parent class (Person) and initialize the name and age attributes
        self.salary = salary # this will initialize the salary attribute of the employee class

    def get_salary(self):
        return f"My salary is {self.salary}."

employee1 = employee("Mauricio", 23, 50000)
print(employee1.greet()) # Output: Hello, my name is Mauricio and I am 23 years old.
print(employee1.get_salary()) # Output: My salary is 50000.

# for each child class, we can override the methods of the parent class to provide a different implementation. For example:
class employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age) # this will call the constructor of the parent class (Person) and initialize the name and age attributes
        self.salary = salary # this will initialize the salary attribute of the employee class

    def greet(self):
        return f"Hello, my name is {self.name}, I am {self.age} years old and I am an employee with a salary of {self.salary}."
employee1 = employee("Mauricio", 23, 50000)
print(employee1.greet()) # Output: Hello, my name is Mauricio, I am
# 23 years old and I am an employee with a salary of 50000.
# Now, we could create a abstract class that will be the parent class of all the classes that we want to create, and we could define abstract methods that will be implemented by the child classes. For example:
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        return "Woof!"
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
dog = Dog()
cat = Cat()
print(dog.make_sound()) # Output: Woof!
print(cat.make_sound()) # Output: Meow!

# In a abstract class, it is not possible to create an object of the class, but we can create an object of the child class that inherits from the abstract class and implements the abstract methods.
# this childs classes dont need to implement all the methods of the parent class, but they need to implement the abstract methods, otherwise they will be considered abstract classes and we will not be able to create objects of those classes.
