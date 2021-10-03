

'''my_dict = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
value = 12
for key in my_dict:
  print(key)
  print(my_dict[key])
  if my_dict[key] == value:
    print("True")
  else:
    print("false")'''
#Solution 1:
if __name__ == '__main__':

  my_dict = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
  value = 12
  res = all(val==value for val in my_dict.values())
  print(res)

#Solution2

my_dict = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
count = 0
x = 10
for val in my_dict.values():
    if val == x:
      count   = count + 1
if count ==len(my_dict):
  print(count)
  print("TRUE")
else:
  print("FALSE")

