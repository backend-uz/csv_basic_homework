def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    len_row = 0
    for i in data:
        len_row += 1
    return len_row

# Read the csv file
import csv
f = open('data.csv', 'r')
d = csv.reader(f)
print(find_number_of_rows(d))