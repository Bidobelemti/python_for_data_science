# In this chapter, we will learn about the basic concepts of Python programming language. We will cover the following topics:
# 3.1 Conditional Statements
# 3.1.1 If Statement
# The if statement is used to execute a block of code if a condition is true. The syntax for the if statement is as follows:
"""
if condition:
    # block of code to be executed if the condition is true
else:
    # block of code to be executed if the condition is false
"""
# Example:
money = 100
# we want to buy a book that costs 50
if money >= 50:
    print("You can buy the book")
else:
    print("You don't have enough money to buy the book")

# How operators work in conditional statements?
# We can use comparison operators to compare values in conditional statements. The comparison operators are as follows
# == : equal to
# != : not equal to
# > : greater than
# < : less than
# >= : greater than or equal to
# <= : less than or equal to
# We can also use logical operators to combine multiple conditions in conditional statements. The logical operators are as follows
# and : returns True if both conditions are true
# or : returns True if at least one condition is true
# Example:
age = 25
if age >=18 and age < 65:
    print("You are an adult")
elif age >= 65:
    print("You are a senior citizen")
else:    \
    print("You are a minor")
# 3.2 Loops
#  Loops are used to execute a block of code repeatedly. In Python, we have two types of loops: for loop and while loop.
# 3.2.1 For Loop
# The for loop is used to iterate over a sequence (such as a list, tuple, string, etc.) or other iterable objects. The syntax for the for loop is as follows:
"""for variable in sequence:
    # block of code to be executed for each item in the sequence
"""
# Example:
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
# if we want to get the index of each item in the sequence, we can use the enumerate() function
for index, fruit in enumerate(fruits):
    print(index, fruit)
# so, the enumerate() function returns a tuple containing the index and the value of each item in the sequence. We can also specify a starting index for the enumerate() function by passing an optional argument. For example, if we want to start the index from 1 instead of 0, we can do it like this:
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
# if we want to use for statement to iterate over a range of numbers, we can use the range() function. The syntax for the range() function is as follows:
# range(start, stop, step)
# The start parameter is the starting number of the sequence (inclusive), the stop parameter is the ending number of the sequence (exclusive), and the step parameter is the increment between each number in the sequence (optional, default is 1).
# Example:
for i in range(5):
    print(i)
# 3.2.2 While Loop
# The while loop is used to execute a block of code as long as a condition is true. The syntax for the while loop is as follows:
"""while condition:
    # block of code to be executed as long as the condition is true
"""
# Example:
count = 0
while count < 5:
    print(count)
    count += 1
# BE CAREFUL: If the condition in the while loop is always true, it will create an infinite loop. For example:
# while True:
#     print("This is an infinite loop")
# To avoid infinite loops, we can use a break statement to exit the loop when a certain condition is met. The break statement is used to exit the loop immediately. The syntax for the break statement is as follows:
"""while condition:
    # block of code to be executed as long as the condition is true
    if some_condition:
        break
"""
# Example:
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
# We can also use a comparison operator to exit the loop when a certain condition is met. For example:
count = 0
while count < 5:
    print(count)
    count += 1
# 3.3 Functions
# A function is a block of code that performs a specific task. In Python, we can define a function using the def keyword. The syntax for defining a function is as follows:
"""def function_name(parameters):
    # block of code to be executed when the function is called
    return value
"""
# Example:
def greet(name):
    return f"Hello, {name}!"
print(greet("Mauricio"))
# We can also define a function that takes multiple parameters. For example:
def add(a, b):
    return a + b
print(add(5, 3))
# We can also define a function that takes default parameters. For example:
def greet(name="World"):
    return f"Hello, {name}!"
print(greet()) # Output: Hello, World!
print(greet("Mauricio")) # Output: Hello, Mauricio!
# We can also define a function that takes variable-length arguments. For example:
def sum(*args):
    total = 0
    print(args) # this will print the tuple of arguments passed to the function\
    print(*args)
    for num in args:
        total += num
    return total
print(sum(1, 2, 3, 4, 5)) # Output: 15
# A function can also return multiple values. For example:
def get_name_and_age():
    name = "Mauricio"
    age = 23
    return name, age

name, age = get_name_and_age()
print(name) # Output: Mauricio
print(age) # Output: 23
# A function could be defined inside another function. This is called a nested function. For example:
def outer_function():
    def inner_function():
        return "Hello from the inner function!"
    return inner_function()
print(outer_function()) # Output: Hello from the inner function!
# We can also use lambda functions to create anonymous functions. A lambda function is a small anonymous function that can take any number of arguments but can only have one expression. The syntax for a lambda function is as follows:
# lambda arguments: expression
# Example:
square = lambda x: x ** 2
print(square(5)) # Output: 25
# Finally we can create a recursive function that calls itself. For example:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5)) # Output: 120
