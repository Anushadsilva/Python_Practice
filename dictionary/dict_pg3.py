#Write a Python script to check whether a given key already exists in a dictionary.

#Solution:
if __name__ == '__main__':
    my_dict = {"1":"Tom","2":"tcm"}
    if "3" in my_dict:
        print("present")
    else:
         print("Not present")