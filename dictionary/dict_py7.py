if __name__ == '__main__':
    my_dict = {1:"red",2:"green",3:"yellow"}
    my_dict1 = {}
    for x in my_dict:
        count = 0
        count = len(my_dict[x])
        key = my_dict[x]
        my_dict1[key] = count
    print(my_dict1)