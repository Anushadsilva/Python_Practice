#Write a Python function to multiply all the numbers in a list.

def my_fuc():
    my_list = (8, 2, 3, -1, 7)
    total = 1
    for x in my_list:
        total = x * total
    return total



if __name__ == '__main__':
  final = my_fuc()
  print("mul of the given numbers is: ", final)