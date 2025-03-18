import pandas as pd 

#print(pd.__version__)

# creting a list to be used as index 
lst_index = list(range(169))
#print(lst_index)

# creating a dataframe from csv file and inserting index with it  
df_csv_1 = pd.read_csv('data.csv')
# print(df_csv_1)
# print(df_csv_1.to_string()) 

df_csv_1.set_index(pd.Index(lst_index), inplace= True)
# print(df_csv_1)

#print(pd.options.display.max_rows)

