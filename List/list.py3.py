#Write a Python program to remove consecutive duplicates of a given list. Go to the editor
Original list:
[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
After removing consecutive duplicates:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]

#solution
if __name__ == '__main__':
    list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
    new_list = []
    for x in range(len(list)-1):
        y = 1 + x
        if list[x] == list[y]:
            if not list[x] in new_list:
                new_list.append(list[x])
        else:
            if not list[x] in new_list:
                new_list.append(list[x])

    print(new_list)