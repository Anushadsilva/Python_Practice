if __name__ == '__main__':
    my_lst1 = ['S001', 'S002', 'S003', 'S004']
    my_lst2 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
    my_lst3 = [85, 98, 89, 92]
    my_newdict1 = {}
    for x in range(len(my_lst1)):
        my_newdict2 = {}
        my_newdict2[my_lst2[x]] = my_lst3[x]
        my_newdict1[my_lst1[x]] = my_newdict2
    print(my_newdict1)