def read_dat_file(filename):
    with open(filename, 'r') as f:
        # read the first line and extract the number of values
        first_line = f.readline().strip()
        print("sequence's size: " + first_line)
        # read the second line and extract the values
        line2 = f.readline().strip()
        values = list(map(int, line2.split()))
    return values