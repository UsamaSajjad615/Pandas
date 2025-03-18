import pandas as pd

df_from_csv = pd.read_csv('data_for_cleaning.csv')
# print(df_from_csv)

# droping the empty values from dataframe
new_df = df_from_csv.dropna()
# print(new_df)

# dropping the empty values from datafram inplace
# df_from_csv.dropna(inplace = True) 
# print(df_from_csv)

# replace the empty values with 130
df_from_csv.fillna('new value', inplace = True)
print(df_from_csv)

# filling the empty values in a column
df_from_csv["calories"].fillna(130, inplace = True)

# filling the empty values in a column with mean value
x = df_from_csv["Calories"].mean()
df_from_csv["Calories"].fillna(x, inplace = True)

# filling the empty values in a column with median value
x = df_from_csv["Calories"].median()
df_from_csv["Calories"].fillna(x, inplace = True)

# filling the empty values in a column with mode value
x = df_from_csv["Calories"].mode()
df_from_csv["Calories"].fillna(x, inplace = True)

##################### CLEANING WRONG FORMAT ################

data_frame = pd.read_csv('data.csv')
data_frame.loc[7, 'Duration'] = 45

for x in data_frame.index:
  if data_frame.loc[x, 'Duration'] > 120:
    data_frame.drop(x, inplace = True)

##################### REMOVING DUPLICATES ################

data_frame.drop_duplicates(inplace = True)