from csv import reader

if __name__ == '__main__':
    with open('prog.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        for row in csv_reader:
            print(row)