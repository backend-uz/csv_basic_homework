#Define function,Get coloumn names from a csv file
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    return list(data)[0]
    
# Read the csv file
import csv 
f = open('data.csv', 'r')
d = csv.reader(f)
print(get_column_names(d))