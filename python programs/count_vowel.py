'''y = input("Enter the string: ")
count = 0
vowel = "AEIOUaeiou"
for i in y:
    if i in vowel:
        count = count + 1
print("vowel counted: ", count)'''


'''lst = [1,2,3,4,5]
for i in range(len(lst)):
   print(lst[i], end=", ")'''

y = input("Enter the string: ")
count = 0
vowel = "AEIOUaeiou"
for i in y:
   if i in vowel:
      count = count + 1
      print("The vowels are: ", count)
   else:
      count = count + 1
      print("The consonant are: ", count)