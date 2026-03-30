# 4.3 numpy: Numerical Computing in Python
# numpy is a library for numerical computing in Python, providing support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays
# to use numpy, we need to import it first
import numpy as np  # we import numpy and give it the alias 'np' for convenience
# we can create a numpy array from a list
array = np.array([1, 2, 3, 4, 5])  # we create a numpy array from a list of numbers
print(array)  # we print the array to see its contents
# we can also create a 2-dimensional array (matrix) from a list of lists
matrix = np.array([[1, 2, 3], [4, 5,6], [7, 8, 9]])  # we create a 2D array (matrix) from a list of lists
print(matrix)  # we print the matrix to see its contents
# numpy provides a wide range of mathematical functions that can be applied to arrays
# for example, we can calculate the mean of an array
mean = np.mean(array)  # we calculate the mean of the array
print(mean)  # we print the mean to see the result
# we can also calculate the standard deviation of an array
std_dev = np.std(array)  # we calculate the standard deviation of the array
print(std_dev)  # we print the standard deviation to see the result
# numpy also provides functions for performing operations on arrays, such as element-wise addition, multiplication,
# and more complex operations like matrix multiplication
# for example, we can perform element-wise addition of two arrays
array1 = np.array([1, 2, 3])  # we create the first array
array2 = np.array([4, 5, 6])  # we create the second array
result = array1 + array2  # we perform element-wise addition
print(result)  # we print the result to see the outcome
# we can also perform matrix multiplication
matrix1 = np.array([[1, 2], [3, 4]])  # we create the first matrix
matrix2 = np.array([[5, 6], [7, 8]])  # we create the second matrix
matrix_result = np.dot(matrix1, matrix2)  # we perform matrix multiplication using the dot function
print(matrix_result)  # we print the result of the matrix multiplication to see the outcome 

# numpy is a powerful library for numerical computing in Python, and it is widely used in data science, machine learning, and scientific computing for its efficiency and ease of use when working with large datasets and complex mathematical operations.
# numpy can define a type of data, for example, we can create an array of integers or an array of floats
int_array = np.array([1, 2, 3], dtype=int)  # we create an array of integers
float_array = np.array([1.0, 2.0, 3.0], dtype=float)  # we create an array of floats
print(int_array)  # we print the integer array to see its contents
print(float_array)  # we print the float array to see its contents
# also we can define the storage size of the data, for example, we can create an array of 8-bit integers or an array of 64-bit floats
int8_array = np.array([1, 2, 3], dtype=np.int8)  # we create an array of 8-bit integers
float64_array = np.array([1.0, 2.0, 3.0], dtype=np.float64)  # we create an array of 64-bit floats
print(int8_array)  # we print the 8-bit integer array to see its contents
print(float64_array)  # we print the 64-bit float array to see its contents

# we can combine different types of data in a single array, but it will be converted to a common type
mixed_array = np.array([1, 2.0, '3'])  # we create an array with mixed types (integer, float, and string)
print(mixed_array)  # we print the mixed array to see its contents

# we can combine numpy with pandas to perform data analysis, for example, we can create a DataFrame from a numpy array
import pandas as pd  # we import pandas to work with DataFrames
data = np.array([[1, 'Alice', 25], [2, 'Bob', 30], [3, 'Charlie', 35]])  # we create a numpy array with data for a DataFrame
df = pd.DataFrame(data, columns=['ID', 'Name', 'Age'])  # we create a DataFrame from the numpy array, specifying column names
print(df)  # we print the DataFrame to see its contents

# we can combine numpy with matplotlib to create visualizations, for example, we can create a simple line plot using numpy arrays
