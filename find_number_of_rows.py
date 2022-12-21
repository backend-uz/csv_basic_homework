def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    d = data.split('\n')

    return len(d)
# Read the csv file
f = open('data.csv', 'r')
r = f.read()
print(find_number_of_rows(r))