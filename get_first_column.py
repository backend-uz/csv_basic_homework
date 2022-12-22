def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    column = []
    for i in data.split('\n'):
        column.append(i.split(',')[0])
    return column[0:-1]

# Read the csv file
f = open('data.csv', 'r')
r = f.read()
print(get_first_column(r))