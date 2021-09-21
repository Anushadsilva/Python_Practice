#Write a Python function to find the Max of three numbers

def mx(x,y,z):
  return max(x,y,z)



if __name__ == '__main__':
  a = int(input("Enter the first number"))
  b = int(input("Enter the second number"))
  c =int(input("Enter the third number"))
  print("max of the given numbers is: ", mx(a,b,c))
