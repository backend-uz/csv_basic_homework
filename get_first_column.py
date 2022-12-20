def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    row = []
    d = data.split('\n')
    for i in d:
     row.append(i.split(',')[0])
    return row

# Read the csv file
f = open('data.csv', 'r')
r = f.read()
print(get_first_column(r))