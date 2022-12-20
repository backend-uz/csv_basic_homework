def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    d = data.split('\n')
    l = d[0].split(',')

    return len(l)

# Read the csv file
f = open('data.csv')
r = f.read()
print(find_number_of_columns(r))