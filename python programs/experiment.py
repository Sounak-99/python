x = input("Enter the long form: ")
l = x.split()
print("The split form is: ", l)
result = ""
for i in l:
    result += i[0]
print("the short form is: ", result)

print("\n")

o = input("Enter the short form: ")
k = o
if k == result:
  print("The full form of the short form: ", " ".join(l))
else:
  print("you gave the wrong short form: ")

