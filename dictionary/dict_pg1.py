''' Python_Practice
# Write a Python program to find all keys in the provided dictionary that have the given value.
# Sample Output:
# Original dictionary elements:
# {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# Find all keys in the said dictionary that have the specified value:
# ['Roxanne', 'Betty'] '''

#Solution
if __name__ == '__main__':
    my_dictn = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
    my_nw_lst = []
    for x in my_dictn:
        if my_dictn[x] == 20:
            my_nw_lst.append(x)
    print(my_nw_lst)