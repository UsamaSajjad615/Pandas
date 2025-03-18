import pandas as pd

# check pandas version
print(pd.__version__)


# creating a series from a list
list_1 = [1,2,3,4,5,6,7,8,9]
series_1 = pd.Series(list_1)
#print(series_1)

# adding labels to a series elements
list_2 = [1,2,3,4,5]
labels = ["a","b","c","d","e"]
series_2 = pd.Series(list_2, index = labels)
#print(series_2["b"])

# creating pandas series from a dictionary
calories_dict = {"day1": 420,"day2":380,"day3":390}
series_3 = pd.Series(calories_dict)
#print(series_3)

#creating a new series from previous series
series_4 = pd.Series(series_3 , index = ["day1","day2"])

#creating dataframe from two series
dataset_1 = {
    "calories" : [420, 380, 390],
    "duration" : [50, 40, 45]
}
dataframe_1 = pd.DataFrame(dataset_1)



# creating  dataframe from dictionary
dataset_2 = {
    "cars" : ["BMW", "VOLVO", "FORD"],
    "passings" : [3, 7, 2]
}
dataframe_2 = pd.DataFrame(dataset_2)


# locating a row in datafram 
# refer to a row index
#print(dataframe_1.loc[0])

#using a list of indexes (note : result would also be a pandas dataframe)
#print(dataframe_1.loc[[0,1]])

# adding index to a dataframe 
dataset_3 = {
    "calories" : [420, 380, 390],
    "duration" : [50, 40, 45]
}
dataframe_3 = pd.DataFrame(dataset_3 , index = ["day1","day2","day3"])

# locating named indexes
#print(dataframe_3.loc["day2"])

