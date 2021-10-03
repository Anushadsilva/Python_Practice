'''Write a Python program to check if a specific Key and a value exist in a dictionary. Go to the editor
Original dictionary:
[{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
 {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'},
 {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]'''

#Solution:
if __name__ == '__main__':
  my_list = [{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]

  key = input("Enter key")
  value = input("Enter vaue")
  for x in my_list:
    print (x)
    if key in x and x[key] == value:
      print(key)
      print(x[key])
      print("Present")
    else:
      print("not present")