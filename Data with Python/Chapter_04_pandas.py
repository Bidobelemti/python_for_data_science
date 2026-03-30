# 4. Working with Data in Python
# we introduce the pandas library, which is a powerful tool for data manipulation and analysis in Python
# we will learn how to create and manipulate DataFrames, which are the main data structure in
# pandas, and how to read and write data using pandas
# 4.2 Introduction to pandas
# pandas is a library that provides data structures and functions for working with structured data
# to use pandas, we need to import it first
import pandas as pd  # we import pandas and give it the alias 'pd' for convenience
# the main data structure in pandas is the DataFrame, which is a 2-dimensional labeled data structure that can hold data of different types (like a table in a database or an Excel spreadsheet)
# we can create a DataFrame from a dictionary, where the keys are the column names and
# the values are lists of data for each column
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)  # we create a DataFrame from the dictionary
print(df)  # we print the DataFrame to see its contents

# we can also read data from a CSV file into a DataFrame using the read_csv() function
df_csv = pd.read_csv('Data with Python\\data\\example.csv')  # we read a CSV file into a DataFrame
print(df_csv)  # we print the DataFrame to see its contents
# we can write a DataFrame to a CSV file using the to_csv() function
df.to_csv('Data with Python\\data\\output.csv', index=False)  # we write the DataFrame to a CSV file, index=False means we don't want to write the row indices to the file