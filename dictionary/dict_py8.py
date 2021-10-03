if __name__ == '__main__':
    my_dict = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
    my_dict2 = {}
    for x in my_dict:
        if my_dict[x] > 170 :
            my_dict2[x] = my_dict[x]
    print(my_dict2)