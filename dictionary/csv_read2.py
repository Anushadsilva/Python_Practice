from csv import reader

if __name__ == '__main__':
    with open('prog1.csv', 'r') as emp_obj:
    # pass the file object to reader() to get the reader object
        csv_emp = reader(emp_obj)
        my_dict = {}
        header = next(csv_emp)
        if header != None:
            list = []
            for row in csv_emp:
                my_dict1 = {}
                my_dict1['empId'] = row[0]
                my_dict1['empname'] = row[1]
                my_dict1['dept_id'] = row[2]
             #   print(my_dict1)
                list.append(my_dict1)
            #print(list)
    with open('dept1.csv', 'r') as dept_obj:
        # pass the file object dj  to reader() to get the reader object
        csv_dept = reader(dept_obj)
        header1 = next(csv_dept)
        # Pass reader object to list() to get a list of lists
        if header != None:
            #list1 = []
            my_dictnw = {}
            for row1 in csv_dept:
              #  my_dict2 = {}
              #  my_dict2['dept_id'] = row1[0]
              #  my_dict2['DeptName'] = row1[1]
              #  list1.append(my_dict2)
                my_dictnw[row1[0]] = row1[1]
                print(my_dictnw)
            #print(list1)
             #   print(my_dict2)
            # print(type(row))
    for x in list:
           if x['dept_id'] in my_dictnw:
               x['DeptName'] = my_dictnw[x['dept_id']]
             #   break

    print(list)

