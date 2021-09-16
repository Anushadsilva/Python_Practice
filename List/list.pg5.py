'''Write a Python program to extract specified size of strings from a give list of string values. Go to the editor
Original list:
['Python', 'list', 'exercises', 'practice', 'solution']
length of the string to extract:
8 '''

#Solution:
if __name__ == '__main__':
  list1 = ['Python', 'list', 'exercises', 'practice', 'solution']
  list2 = []
  usr = input("choose the length of string 6 or 4 or 9 or 8")
  for ch in list1:
    if len(ch) == int(usr):
      list2.append(ch)
  print(list2)