'''str = "python"
for ch in str:
    print(ch, end = ",")

strr = "java"
print("\n")
index = 0
while index < len(strr):
    print(strr[index], end="," )
    index = index + 1


st1 = "hello"
st2 = "world"
print("\n")
result = st1+" "+st2
print(result)

ss = input("Enter the string: ")
ss2 = input("Enter the string: ")
print("\n")
result = ss+" "+ss2
print(result)

sk = "hello"
print("\n")
result = sk*3
print(result)

stt = "python"
print("python" in stt)
print("c" not in stt)

gg = "hello"
print("\n")
print(len(gg))

stk = "python"
print("\n")
print(stk.count("t"))
print("\n")
hh = "hello world"
print("\n")
print(hh.find("python"))


gk = "PYoHON"
print(gk.isalpha())

jj = "12345fghk"
lk = "123456789"
print(jj.isdigit())
print(lk.isdigit())

hu = "12345kkl"
po = "11116543"
print(hu.isalnum())
print(po.isalnum())

mm = "  "
uu = ""
print(mm.isspace())
print(uu.isspace())

tk = "sounak basak"
print(tk[:-3])


yy = "python"
print(yy.islower())
print(yy.upper())


gh = "JAVA"
print(gh.isupper())
print(gh.lower())

no = "india"
print(no.capitalize())

yes = "india is my country"
print(yes.title())


rt = "      sfkjsfk      "
gui = "      hhhhh"
cui = "huiiiiiiiiii      "
print(rt.strip())
print(gui.lstrip())
print(cui.rstrip())



x = input("Enter the full form: ")
l = x.split()
print("The split form of the string:- ", l)
print("The short form of the string:- ",)
for i in l:
    print(i[0], end="")
print("\n")
o = input("Enter the small form: ")
p = o
for i in p:
    print(p)
if o == p:
  print("The full form of the short form:- ", ' '.join(l))
else:
  print("you gave the wrong short form")



fg = "sounak basak"
print(fg.partition(" "))

fk = "abcdbadcf"
print(fk.replace("b", "x"))


gu = "sounak basak"
print(gu.startswith("s"))
print(gu.endswith("k"))
print(gu.startswith("o"))
print(gu.endswith("s"))'''

'''list = ['a', 'b', 'c', 'd', 'e']
index = 0
while index < len(list):
    print(list[index], end='')
    index = index + 1

for item in list:
    print(item,end='')'''

'''list1 = [1,2,1]
list2 = [1,2,1,1]
print(list1 < list2)'''

'''lst1 = [1,2,3]
lst2 = ['a','b','c']
print(lst1 + lst2)
for i in lst2:
    lst1.append(lst2)
print(lst1)'''

'''list1 = [1,2,3]
list2 = ['a','b','c']
list1.append(list2)
print(list1)
list1.extend(list2)
print(list1)'''

'''original_list = [1,2,3]
copy_list = original_list.copy()
slicing_list = original_list[ : ]
list_list = list(original_list)
reference_list = original_list

copy_list[0] = 20
print(original_list)
print(copy_list)

list_list[2] = 30
print(original_list)
print(list_list)

slicing_list[1] = 20
print(original_list)
print(slicing_list)

reference_list[1] = 20
print(original_list)
print(reference_list)'''


'''lst = ["sounak"]
lst.append("basak")
print(lst)'''

'''num = [1,2,3]
num.extend([3,4,5])
print(num)'''

'''num = [1,2,3,4,5,6]
print(num.index(6))
print(num.index(8))'''

'''lst = ['a', 'b', 'a', 'c', 'b', 'a']
print(lst.count('a'))'''

'''lst = ['a','b','c','d']
lst.insert(4, 'fuck')
print(lst)'''

'''lst = [1,2,3,4,5]
x = input("Enter the string to reverse: ")
list2 = []
lst.reverse()
print(lst)
lst.reverse()
list2.append(x)
list2.reverse()
print(list2)'''

'''lst = [1,2,3,4,5]
print(lst.pop())
print(lst.pop(2))
print(lst)'''

'''lst = [1,2,3,4,5]
print(lst.remove(1))
print(lst)'''

'''lst = [1,2,3,4,5]
del lst[2]
print(lst)
del lst
print(lst)'''

'''lst = [1,2,3,4,5]
lst.clear()
print(lst)'''


'''lst = [3,5,1,8,7]
lst.sort()
print(lst)

lst = [3,5,1,8,7]
sorted_list = sorted(lst)
print(sorted_list)
print(lst)'''


lst = [3,5,1,8,7]
lst.sort(reverse=True)
print(lst)