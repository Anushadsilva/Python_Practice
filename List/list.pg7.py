'''To get max and min from '''


if __name__ == '__main__':
    list = [3, 5, 6, 2, 1, 9, 7]

    max = list[0]
    min = list[0]
    for x in list:
        if x > max:
            max = x
        elif x < min:
                min = x
    print(max)
    print(min)