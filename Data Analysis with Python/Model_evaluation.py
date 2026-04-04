# Model Evaluation
# We have two main types of model evaluation techniques: 1. train/test split and 2. cross-validation.
# Train/Test Split
# Train/test split is a technique where we split the dataset into two parts: a training set and a 
# testing set. We use the training set to train the model and the testing set to evaluate the model's performance. 
# The most common split is 80% for training and 20% for testing, but this can be adjusted based on the size of the dataset 
# and the specific requirements of the problem.
from sklearn.model_selection import train_test_split  # we import train_test_split to split the dataset into training and testing sets
from sklearn.linear_model import LinearRegression  # we import LinearRegression to create a linear regression model
from sklearn.metrics import mean_squared_error  # we import mean_squared_error to evaluate the performance of the model
import numpy as np  # we import numpy to work with arrays
np.random.seed(0)  # we set a random seed for reproducibility
# we create a synthetic dataset for demonstration purposes
X = np.random.rand(100, 1)  # we create a feature matrix with 100 samples and 1 feature
y = 2 * X + 1 + np.random.rand(100, 1)  # we create a target variable with a linear relationship to the feature, plus some random noise
# we split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)  # we split the dataset into training and testing sets with an 80/20 split
# we create a linear regression model and fit it to the training data
model = LinearRegression()
model.fit(X_train, y_train)
# we make predictions on the testing data
y_pred = model.predict(X_test)
# we evaluate the model's performance
mse = mean_squared_error(y_test, y_pred)  # we calculate the mean squared error of the model's predictions
print("Mean Squared Error:", mse)  # we print the mean squared error to evaluate the model's performance

# Cross-Validation
# Cross-validation is a technique where we split the dataset into k folds (usually 5 or 10) and 
# train the model k times, each time using a different fold as the testing set and the remaining folds as the training set.
from sklearn.model_selection import cross_val_score  # we import cross_val_score to perform cross-validation
# we create a linear regression model
model = LinearRegression()
# we perform cross-validation and calculate the mean squared error for each fold
cv_scores = cross_val_score(model, X, y, cv=5, scoring='neg_mean_squared_error')  # we perform 5-fold cross-validation and calculate the negative mean squared error for each fold
print("Cross-Validation Scores (Negative MSE):", cv_scores)  # we print the cross-validation scores to evaluate the model's performance across different folds
print("Average Cross-Validation Score (Negative MSE):", np.mean(cv_scores))  # we print the average cross-validation score to evaluate
# the overall performance of the model across all folds
# Overfitting, Underfitting, and Model Selection
# Overfitting occurs when a model learns the training data too well, including the noise, and performs poorly on unseen data. 
# Underfitting occurs when a model is too simple to capture the underlying patterns in the data, resulting in poor performance on
# both the training and testing sets. Model selection involves choosing the best model based on its performance on the testing set 
# or through cross-validation, while also considering factors such as complexity and interpretability.
# Ridge Regression
# Ridge regression is a linear regression technique that includes a regularization term to prevent overfitting by adding a penalty for large coefficients.
from sklearn.linear_model import Ridge  # we import Ridge to create a ridge regression model
# we create a ridge regression model with a regularization strength of 1.0
ridge_model = Ridge(alpha=1.0)
ridge_model.fit(X_train, y_train)  # we fit the ridge regression model to the training data
y_pred_ridge = ridge_model.predict(X_test)  # we make predictions on the testing
mse_ridge = mean_squared_error(y_test, y_pred_ridge)  # we calculate the mean squared error of the ridge regression model's predictions
print("Mean Squared Error (Ridge Regression):", mse_ridge)  # we print the mean squared error of the ridge regression model to evaluate its performance
# Grid Search
# Grid search is a technique for hyperparameter tuning that involves exhaustively searching through a specified grid of hyperparameters to find the best combination for a given model.
from sklearn.model_selection import GridSearchCV  # we import GridSearchCV to perform grid search for hyperparameter tuning
# we create a ridge regression model
ridge_model = Ridge()
# we define a grid of hyperparameters to search through
param_grid = {'alpha': [0.1, 1.0, 10.0]}  # we define a grid of alpha values for the ridge regression model
# we perform grid search with 5-fold cross-validation to find the best hyperparameters
grid_search = GridSearchCV(estimator=ridge_model, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error')  # we perform grid search with 5-fold cross-validation and calculate the negative mean squared error for each combination of hyperparameters
grid_search.fit(X, y)  # we fit the grid search to the entire dataset to
print("Best Hyperparameters:", grid_search.best_params_)  # we print the best hyperparameters found by the grid search to evaluate the model's performance with the optimal settings
