def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    return list(data)[0]
    
# Read the csv file
import csv
f = open('data.csv', 'r')
r = csv.reader(f)
print(get_first_column(r))