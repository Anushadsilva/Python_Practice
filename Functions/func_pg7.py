#Write a Python function that takes a list and returns a new list with unique elements of the first list.

def my_rtn():
    my_list = [1,2,3,3,3,3,4,5]
    nw_list = []
    for x in my_list:
        if not x in nw_list:
            nw_list.append(x)
    return nw_list


if __name__ == '__main__':
    nw_lst = my_rtn()
    print(nw_lst)


