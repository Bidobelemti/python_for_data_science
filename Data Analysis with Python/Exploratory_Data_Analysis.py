# Exploratory Data Analysis
# Exploratory Data Analysis (EDA) is the process of analyzing and summarizing a dataset to understand its main characteristics, often using visual methods. EDA is an important step in the data analysis process as it helps to identify patterns, detect anomalies, test hypotheses, and check assumptions with the help of summary statistics and graphical representations.
# We can use pandas and matplotlib to perform EDA in Python.
import pandas as pd  # we import pandas to work with DataFrames
import matplotlib.pyplot as plt  # we import matplotlib to create visualizations
import scipy as sp  # we import scipy to perform statistical analysis
import seaborn as sns  # we import seaborn to create more advanced visualizations
import asyncio  # we import asyncio to handle asynchronous operations, such as downloading data from a URL
import requests  # we import requests to make HTTP requests to download data from a URL
from pyodide.http import pyfetch  # we import pyfetch to fetch data from a URL

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv"

response = requests.get(url)
path = "Data Analysis with Python/data/automobileEDA.csv"
if response.status_code == 200:
    with open(path, "wb") as f:
        f.write(response.content)

print("Download completed successfully!")
# we can read the dataset into a DataFrame
df = pd.read_csv(path)  # we read the CSV file into a DataFrame
print(df.head())  # we print the first few rows of the DataFrame to see its
print(df.info())  # we print information about the DataFrame, including column names and data types
print(df.describe())  # we print a summary of the DataFrame to see the distribution of the data
print(df.dtypes)  # we print the data types of the columns in the DataFrame to see what types of data we are working with

#1. What is the data type of the column 'peak-rpm'?
print(df['peak-rpm'].dtype)  # we print the data type of the 'peak-rpm' column to see what type of data it contains
#2. Find the correlation between the following columns: bore, stroke, compression-ratio and horsepower
correlation = df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr()  # we calculate the correlation between the specified columns
print(correlation)  # we print the correlation matrix to see the relationships between the columns
#3. Find the correlation between x:stroke and y: price
stroke_price_corr = df[['stroke', 'price']].corr() # Correlation stroke-price, we could obtain a correlation between to columns on the dataset
print(stroke_price_corr)
sns.regplot(x='stroke', y='price', data=df)  # we create a regression plot to visualize the relationship between 'stroke' and 'price'
plt.title('Correlation between Stroke and Price')  # we set the title of the plot
plt.xlabel('Stroke')  # we set the label for the x-axis
plt.ylabel('Price')  # we set the label for the y-axis
plt.show()  # we display the plot to see the relationship between 'stroke' and 'price'

#4. Use the groupby function to find the avg price of each car based on body-style
df_gptest2 = df[['body-style','price']] # we create a new DataFrame with only the 'body-style' and 'price' columns to perform the groupby operation
print(df_gptest2.head())  # we print the first few rows of the new Data Frame to see its contents
grouped_test_bodystyle = df_gptest2.groupby(['body-style'],as_index= False).mean() # we group the DataFrame by 'body-style' and calculate the mean price for each body style, setting as_index to False to keep 'body-style' as a column in the resulting DataFrame
print(grouped_test_bodystyle) # we print the grouped DataFrame to see the average price for each body style