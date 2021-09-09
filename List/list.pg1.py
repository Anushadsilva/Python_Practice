


if __name__ == '__main__':
    color_name = ["Black", "Red", "Maroon", "Yellow"]
    color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]



    my_list = []
    for x in range(len(color_name)):
        my_dict = {"color_name" : color_name[x], "color_code" : color_code[x] }
        my_list.append(my_dict)
    print(my_list)
