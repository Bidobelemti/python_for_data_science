## In this chapter, we will cover the basic concepts of python
# 1. First Hello World Program

print("Hello World")

## Print is a built-in function in python that is used to display the output on the screen

# 2. Variables and Data Types
# Variables are used to store data. In Python, we don't need to declare the type of variable.

val_integer = 10 # this is an integer variable
val_float = 3.14 # this is a float variable
val_string = 'Hello' # this is a string variable. We could use double quotes as well "Hello"
val_boolean = True # this is a boolean variable. It can be either True or False. Also we transform it to 1 or 0 respectively

# we can also use the type() function to check the type of variable

print(type(val_integer)) # Output: <class 'int'>
print(type(val_float)) # Output: <class 'float'>

# 3. Comments
# Comments are used to explain the code. They are ignored by the interpreter. In Python, we can use the # symbol to write a comment.
# This is a single line comment

"""
this is a multi-line comment
we can use triple quotes to write multi-line comments
"""

# 4. Indentation
"""
The indentation is very important in python. It is used to define the scope of loops, functions, and classes.
In python, we use 4 spaces for indentation. We can also use tabs, but it is not recommended.
"""
# if we don't use indentation, we will get an error
# 5. Expressions and Statements
# An expression is a combination of values and operators that can be evaluated to a single value. For example, 2 + 3 is an expression that evaluates to 5.
# A statement is a line of code that performs an action. For example, print("Hello World") is a statement that prints "Hello World" on the screen.
sum = 2 + 3 # this is an expression that evaluates to 5
print(sum) # this is a statement that prints the value of sum on the screen

sum = 2 + 3.0 # this is an expression that evaluates to 5.0 because of the presence of a float
print(sum) # this is a statement that prints the value of sum on the screen

div = 10 / 3 # this is an expression that evaluates to 3.3333333333333335 because of the presence of a float
print(div) # this is a statement that prints the value of div on the screen

# if we want to get the integer division, we can use the // operator
int_div = 10 // 3 # this is an expression that evaluates to 3 because of the presence of the // operator
print(int_div) # this is a statement that prints the value of int_div on the screen

# 6. String Slicing
# String slicing is a technique to extract a portion of a string. We can use the slicing operator [] to slice a string. The syntax for slicing is string[start:stop:step]. The start index is inclusive and the stop index is exclusive. The step is optional and it is used to specify the step size for slicing.

var = '01234567'

print(var[::2])

# We can also use negative indexing to slice a string. The negative indexing starts from the end of the string. The last character of the string has an index of -1, the second last character has an index of -2, and so on.
print(var[::-1]) # this will reverse the string
print(var[1:5]) # this will extract characters from index 1 to 4
print(var[-4:-1]) # this will extract characters from index -4 to -2
print(var[0:3:2]) # this will extract characters from index 0 to 2 with a step size of 2, so it will extract characters at index 0 and 2