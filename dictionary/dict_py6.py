
'''Write a Python program to count the frequency in a given dictionary.
Original Dictionary:
{'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
Count the frequency of the said dictionary:
Counter({10: 2, 40: 2, 20: 2, 70: 1, 80: 1})'''


#Solution
if __name__ == '__main__':
    dict1 = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
    freq = 0
    dict2 = {}
    for x in dict1.values():
        if x in dict2:
            dict2[x] = dict2[x] + 1
        else:
            dict2[x] = 1
    print(dict2)
