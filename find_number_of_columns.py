def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    import csv
    data = csv.reader(f)
    l = list(data)[0]
    return int(len(l))

# Read the csv file
f = open('data.csv')
print(find_number_of_columns(f))