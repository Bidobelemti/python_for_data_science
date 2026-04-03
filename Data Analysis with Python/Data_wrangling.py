# Preprocessing Data
# We consider the following steps in preprocessing data:
# 1. Data Cleaning: This involves handling missing values, removing duplicates, and correcting errors in the data.
# 2. Data Transformation: This includes normalizing or standardizing data, encoding categorical variables, and creating new features from existing ones.
# 3. Data Integration: This step involves combining data from different sources, ensuring consistency and resolving any conflicts in the data.
# 4. Data Reduction: This includes techniques like dimensionality reduction, feature selection, and sampling to reduce the size of the dataset while retaining important information.
# we can use pandas to perform data cleaning, transformation, integration, and reduction
import pandas as pd  # we import pandas to work with DataFrames
# we can read a CSV file into a DataFrame
df = pd.read_csv('Data Analysis with Python/data/healthcare_dataset.csv')  # we read a CSV file into a DataFrame
print(df.head(), '\n', len(df))  # we print the first few rows of the DataFrame to see its contents
# we can handle missing values by filling them with a specific value or dropping them
print('------------------------------------------')
df_filled = df.fillna(0)  # we fill missing values with 0
print(df_filled.head(), '\n', len(df_filled))  # we print the first few rows of the filled DataFrame to see its contents
print('------------------------------------------')
df_dropped = df.dropna()  # we drop rows with missing values
print(df_dropped.head(), '\n', len(df_dropped))  # we print the first few rows of the dropped DataFrame to see its contents
print('------------------------------------------')
# In this case, we can see that the dataset has 55500 rows on all filled, because It don't have any label in blank.
# we can also see a summary of the DataFrame to understand the distribution of the data
print(df.describe())  # we print a summary of the DataFrame to see the distribution of the data
# we can also check for duplicates in the DataFrame
print(df.duplicated().sum())  # we check for duplicates in the DataFrame and print the count
# we can remove duplicates from the DataFrame
df_no_duplicates = df.drop_duplicates()  # we remove duplicates from the DataFrame
print(df_no_duplicates.head(), '\n', len(df_no_duplicates))  # we print the first few rows of the DataFrame without duplicates to see its contents
print('------------------------------------------')
print(df['Room Number'].value_counts())  # we check the value counts of the 'Room Number' column to see the distribution of room numbers

print(df_no_duplicates.isna().sum()) # We check if the dataset's columns have any NaN value

# Now we must to normalize the columns where we can found a any String.
print(df_no_duplicates.info())
# 1. We can see that the 'Patient Name' and 'Diagnosis' columns have string values, so we can normalize them by converting them to lowercase or uppercase.
df_normalize_string = df_no_duplicates.copy()  # we create a copy of the DataFrame to normalize string columns
df_normalize_string['Name'] = df_normalize_string['Name'].str.lower()  # we convert the 'Patient Name' column to lowercase
df_normalize_string['Test Results'] = df_normalize_string['Test Results'].str.lower()  # we convert the 'Test Results' column to lowercase
print(df_normalize_string.head(), '\n', len(df_normalize_string))  # we print the first few rows of the normalized DataFrame to see its contents
# 2. We can also normalize the 'Room Number' column by converting it to a categorical variable or by encoding it as a numerical variable.
df_normalize_string['Room Number'] = df_normalize_string['Room Number'].astype('category')  # we convert the 'Room Number' column to a categorical variable
print(df_normalize_string.info())  # we print the info of the normalized DataFrame to see the data types of the columns
# we can also encode the 'Room Number' column as a numerical variable using one-hot encoding
df_encoded = pd.get_dummies(df_normalize_string, columns=['Medical Condition'])  # we encode the 'Medical Condition' column using one-hot encoding
print(df_encoded.head(), '\n', len(df_encoded))  # we print the first few rows of the encoded DataFrame to see its contents
# we can also create new features from existing ones, for example, we can create a new feature that indicates whether a patient has a certain medical condition
df_encoded['Has Diabetes'] = df_encoded['Medical Condition_Diabetes']  # we create a new feature that indicates whether a patient has diabetes based on the one-hot encoded 'Medical Condition' column
print(df_encoded.head(), '\n', len(df_encoded))  # we print the first few rows of the DataFrame with the new feature to see its contents