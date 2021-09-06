'''Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}'''

#Solution:
if __name__ == '__main__':
  input = 'w3resource'
  output = {}
  for ch in input:
    print(ch)
    if ch in output:
      output[ch] = output[ch] + 1
    else:
      output[ch] = 1
  print(output)