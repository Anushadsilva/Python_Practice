#Write a Python program to create set difference.
if __name__ == '__main__':
    set_x = set([1, 2, "hello", 9])
    set_y = set([1, 3, "hello", "wassup"])
    set_new = set_x - set_y
    print(set_new)