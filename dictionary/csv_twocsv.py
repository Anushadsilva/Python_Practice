from csv import reader

if __name__ == '__main__':
    with open('prog1.csv', 'r') as emp_obj:
        csv_emp = reader(emp_obj)
        header = next(csv_emp)
        if header != None:
            my_dict1 = {}
            for row in csv_emp:
                with open('dept1.csv', 'r') as dept_obj:
                    csv_dept = reader(dept_obj)
                    header1 = next(csv_dept)
                    if header != None:
                        for row1 in csv_dept:
                            if row1[0] not in my_dict1:
                                my_dict1['empId'] = row[0]
                                my_dict1['empname'] = row[1]
                                my_dict1['dept_id'] = row1[0]
                                my_dict1['DeptName'] = row1[1]
                                break
                        print(my_dict1)

