#Write a Python program to reverse a string.

def my_rev():
    str = "1234abcd"
    strnw = str[::-1]
    return strnw


if __name__ == '__main__':
  rev = my_rev()
  print("mul of the given numbers is: ", rev)