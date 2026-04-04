# We will see how to develop a model using the dataset we preprocessed. 
# We learn about: 1. Simple linear regression, 2. model evaluation, 3. polynomial regression, 4. r-squared, 5. prediction and decision making
# Linear and multiple regression are statistical techniques used to model the relationship between a dependent variable and one or more independent variables. In linear regression, we model the relationship between a dependent variable and a single independent variable, while in multiple regression, we model the relationship between a dependent variable and multiple independent variables. Both techniques are widely used in data analysis and machine learning for predicting outcomes and understanding relationships between variables.
# we can use the scikit-learn library to perform linear and multiple regression in Python
import pandas as pd  # we import pandas to work with DataFrames
import numpy as np  # we import numpy for numerical operations
from sklearn.linear_model import LinearRegression  # we import the LinearRegression class from scikit-learn to perform linear regression
np.random.seed(0)  # we set a random seed for reproducibility
# we can create a simple linear regression model using scikit-learn
# we create a sample dataset with a linear relationship between X and y
n = 3 # we define the number of samples
x = np.random.rand(100, 1) * n  # we create an array of 100 random values for the independent variable X, scaled by n
y = 2 * x + 1 + np.random.rand(100, 1) * n  # we create the dependent variable y with a linear relationship to X, adding some random noise
# we create a LinearRegression model and fit it to the data
model = LinearRegression()  # we create an instance of the LinearRegression class
model.fit(x, y)  # we fit the model to the data (X and y
# we can print the coefficients of the model
print("Coefficient (slope):", model.coef_[0][0])  # we print the coefficient (slope) of the linear regression model
print("Intercept:", model.intercept_[0])  # we print the intercept of the linear regression model
# we can also make predictions using the model
y_pred = model.predict(x)  # we make predictions using the fitted model
print("Predicted values:", y_pred[:5])  # we print the first 5 predicted values to see the output of the model
# Model Evaluation using visualization
# we can visualize the original data and the fitted line to evaluate the model
import matplotlib.pyplot as plt  # we import matplotlib to create visualizations
import seaborn as sns  # we import seaborn to create more advanced visualizations
sns.scatterplot(x=x.flatten(), y=y.flatten(), label='Data')  # we create a scatter plot of the original data points
sns.lineplot(x=x.flatten(), y=y_pred.flatten(), color='red', label='Fitted Line')  # we create a line plot of the fitted line from the model
plt.title('Linear Regression Fit')  # we set the title of the plot
plt.xlabel('X')  # we set the label for the x-axis
plt.ylabel('y')  # we set the label for the y-axis
plt.legend()  # we add a legend to the plot
plt.show()  # we display the plot to evaluate the fit of the linear regression model

# Kernel Density Estimation (KDE)
# Kernel Density Estimation (KDE) is a non-parametric way to estimate the probability density function of a random variable. It is used to visualize the distribution of data and can be particularly useful for understanding the underlying structure of the data, identifying patterns, and detecting outliers. KDE works by placing a kernel (a smooth, symmetric function) on each data point and summing these kernels to create a smooth estimate of the density function. In Python, we can use libraries like seaborn or scipy to perform KDE and visualize the results.
# we can use seaborn to create a KDE plot of the data
sns.kdeplot(x=x.flatten(), y=y.flatten(), cmap='Blues', shade=True)  # we create a KDE plot of the data using seaborn
plt.title('Kernel Density Estimation')  # we set the title of the plot
plt.xlabel('X')  # we set the label for the x-axis
plt.ylabel('y')  # we set the label for the y-axis
plt.show()  # we display the KDE plot to visualize the density of the data points

# Polynomial regressions and pipelines
# Polynomial regression is a type of regression analysis that models the relationship between a dependent variable and an independent variable as an nth degree polynomial. It is used when the relationship between the variables is not linear and can capture more complex patterns in the data. In Python, we can use libraries like scikit-learn to perform polynomial regression by transforming the input features into polynomial features and then fitting a linear regression model to these transformed features. Pipelines in scikit-learn allow us to streamline the process of applying multiple transformations and modeling steps in a single workflow, making it easier to manage and evaluate our machine learning models.
from sklearn.preprocessing import PolynomialFeatures  # we import the PolynomialFeatures class from scikit-learn to create polynomial features
from sklearn.pipeline import make_pipeline  # we import the make_pipeline function from scikit-learn
# we can create a polynomial regression model using scikit-learn
degree = 2  # we define the degree of the polynomial features
polynomial_model = make_pipeline(PolynomialFeatures(degree), LinearRegression())  # we create a pipeline that first transforms the input features into polynomial features and then fits a linear regression model
polynomial_model.fit(x, y)  # we fit the polynomial regression model to the data
y_poly_pred = polynomial_model.predict(x)  # we make predictions using the fitted polynomial regression model
# we can visualize the original data and the fitted polynomial curve to evaluate the model
sns.scatterplot(x=x.flatten(), y=y.flatten(), label='Data')  # we create a scatter plot of the original data points
sns.lineplot(x=x.flatten(), y=y_poly_pred.flatten(), color='red', label='Polynomial Fit')  # we create a line plot of the fitted polynomial curve from the model
plt.title('Polynomial Regression Fit')  # we set the title of the plot
plt.xlabel('X')  # we set the label for the x-axis
plt.ylabel('y')  # we set the label for the y-axis
plt.legend()  # we add a legend to the plot
plt.show()  # we display the plot to evaluate the fit of the polynomial regression model
# Measuring the accuracy of the model using R-squared MSE and RMSE
# MSE is the mean of the squared differences between the predicted and actual values, while RMSE is the square root of MSE, providing a measure of the average magnitude of the errors in the same units as the target variable. R-squared is a statistical measure that represents the proportion of the variance in the dependent variable that is explained by the independent variables in the model, with values ranging from 0 to 1, where higher values indicate a better fit of the model to the data.
from sklearn.metrics import mean_squared_error, r2_score  # we import the mean_squared_error and r2_score functions from scikit-learn to evaluate the model
mse = mean_squared_error(y, y_poly_pred)  # we calculate the Mean Squared Error (MSE) between the actual and predicted values
rmse = np.sqrt(mse)  # we calculate the Root Mean Squared Error (RMSE) by taking the square root of MSE
r2 = r2_score(y, y_poly_pred)  # we calculate the R-squared value to evaluate the proportion of variance explained by the model
print("Mean Squared Error (MSE):", mse)  # we print the MSE to see the average squared error of the model's predictions
print("Root Mean Squared Error (RMSE):", rmse)  # we print  the RMSE to see the average magnitude of the errors in the same units as the target variable
print("R-squared:", r2)  # we print the R-squared value to see how well the model explains the variance in the data 