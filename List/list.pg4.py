#Write a Python program to remove consecutive duplicates of a given list. Go to the editor
Original list:
[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
After removing consecutive duplicates:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]

#Solution
if __name__ == '__main__':
    list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
    new_list = []
    prev = 0
    for x in list:
        if x != prev:
            new_list.append(x)
            print(prev)
            print(x)
            prev = x
    print(new_list)
