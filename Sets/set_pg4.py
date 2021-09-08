#Write a Python program to remove item(s) from a given set

#Solution

if __name__ == '__main__':
    set_x = set([1, 2, "hello", 9])
    set_x.pop()
    print(set_x)
    set_x.discard(2)
    print(set_x)
    set_x.remove("hello")
    print(set_x)