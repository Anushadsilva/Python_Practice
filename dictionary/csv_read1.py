from csv import reader

if __name__ == '__main__':
    with open('prog1.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        my_dict = {}
        header = next(csv_reader)
        if header != None:
        # Pass reader object to list() to get a list of lists
            for row in csv_reader:
                my_dict1 = {}
                my_dict1['Name']=row[1]
                my_dict1['Course']=row[2]
                my_dict1['City']=row[3]
                my_dict1['Session']=row[4]
                my_dict[row[0]] = my_dict1
                #print(type(row))
            print(my_dict)
