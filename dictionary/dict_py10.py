if __name__ == '__main__':
    my_dict = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
    my_dictnw = {}
    for x ,y in my_dict.items():
        for z in range(len(y)):
            if (y[z] > 6.0 and y[z] >= 70):
                my_dictnw[x] = my   _dict[x]
    print(my_dictnw)
