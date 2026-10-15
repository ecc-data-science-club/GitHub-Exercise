"""
All of this code works to import and do simple data exploration of a csv file.
Modify the code in the "TODO" section to match their respective comments. Uncomment lines to run code. 
"""


import pandas as pd

# import actors.csv and save into a dataframe called "dataset"
dataset = pd.read_csv("data/actors.csv")

# print the whole dataset
#print(dataset)

# prints the first five rows (0 to 4) of the dataset
#print(dataset.head()) # .head() takes an argument of "number of rows" or defaults to 5

#prints a description of the columns, how many rows there are, their datatypes and how many null values they have
#print(dataset.info())

#prints some statistical values (mean, count, standard deviation, etc) of the numeric columns
#print(dataset.describe())

#prints a specific column 
#print(dataset['Actor'])

#creates a new table of just one column
#dataset_simple = dataset['Actor']
#print(dataset_simple)

# Renames 'Total Gross' to 'Total_Gross' in dataset
dataset = dataset.rename(columns={'Total Gross': 'Total_Gross'})
print(dataset)



# TODO: Fix the following lines so that they align with the comments
# Begin by removing the comment blocks " at the beginning and end of this section

# print the last 15 rows of the dataset
"""Write Code here"""

# Create a new table of just the rows in the column "Actor" and their "#1 movie", then print the whole table
"""Write Code here"""

# Rename '#1 Movie' to 'Top_Movie' in actor_table
"""Write Code here"""

# create a new table called star_wars_movies that only copies rows in "Top_Movie" that contain "Star Wars", then print the table
"""Write Code here"""

