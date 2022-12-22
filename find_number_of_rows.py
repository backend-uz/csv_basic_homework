def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    d = data.split('\n')
    l = d[0:-1]
    return len(l)
# Read the csv file
f = open('data.csv', 'r')
r = f.read()
print(find_number_of_rows(r))