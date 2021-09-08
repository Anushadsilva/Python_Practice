#Write a Python program to add member(s) in a set.

#Solution

if __name__ == '__main__':
    set_x = set([1, 2, "hello", 9])
    set_x.add("wassup")
    set_x.update([1, 5])
    print(set_x)