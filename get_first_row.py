def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   
   return list(data)[1]

# Read the csv file
import csv 
f = open('data.csv', 'r')
d = csv.reader(f)
print(get_first_row(d))