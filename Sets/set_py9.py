#Write a Python program to create a shallow copy of sets.
if __name__ == '__main__':
    set_x = set([1, 2, "hello", 9])
    set_y = set_x.copy()
    print(set_y)