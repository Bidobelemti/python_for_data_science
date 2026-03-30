import pandas as pd
path = 'Data with Python/data/IMDB Dataset.csv'
df_raw = pd.read_csv(path)

print(df_raw.head())
print('------------------------------------------')

print(df_raw.info())
print('------------------------------------------')

print(df_raw[df_raw['review'].duplicated()]) # we can find all duplicated rows, we can delete it or we can storage in a new variable
# if we will delete those rows we can use drop_duplicated()
df = df_raw.drop_duplicates()
print(len(df))

# how we can show a one row?
# it is easy, we do it with ilooc function

print(df.iloc[0])

# if we must show a one column in this row we will do

print(df['review'].iloc[0]) # it isn't the best form for show a specify column
print(df.iloc[0]['review']) # we should do it, first find a row; next, find a column and finally show the result

# The text isn't clean, we can find HTML labes. In data analythics we should clean this data, in this case it isn't a priority
