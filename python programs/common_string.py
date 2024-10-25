string1 = input("Enter the 1st string: ")
string2 = input("Enter the second string: ")

set1 = set(string1)
set2 = set(string2)

common_string = set1.intersection(set2)

if common_string:
    print("common letters are: ", common_string)
else:
    print("no common letters found")