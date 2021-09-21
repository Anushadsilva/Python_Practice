def my_function1(val):
  my_dict = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
  for key in my_dict:
    if my_dict[key] == val:
      return True
    else:
      return False








if __name__ == '__main__':
  a = my_function1(12)
  print(a)
  b = my_function1(10)
  print(b)