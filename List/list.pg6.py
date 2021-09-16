'''Write a Python program to reverse strings in a given list of string values.
Original lists:
['Red', 'Green', 'Blue', 'White', 'Black']
Reverse strings of the said given list:'''


#Solution:
if __name__ == '__main__':
    l1 = ['Red', 'Green', 'Blue', 'White', 'Black']
    new_list = []
    for i in l1:
        new_list.append(i[::-1])
    print(new_list)

#Solution2 :
if __name__ == '__main__':
    l1 = ['Red', 'Green', 'Blue', 'White', 'Black']
    new_list = []
    for i in l1:
        str = ""
        for ch in reversed(i):
            str = str + ch
        new_list.append(str)
    print(new_list)