'''def minimum(a):
    mini = a[0]
    for i in range(len(a)):
        if a[i] < mini:
            mini = a[i]
            i += 1
    return mini



def maximum(a):
    maxi = a[0]
    for i in range(len(a)):
        if a[i] > maxi:
            maxi = a[i]
            i += 1
    return maxi



import array as ar
a = ar.array('i')
n = int(input("Enter the range of the array: "))
for i in range(n):
    ele = int(input("Enter the element of the array: "))
    a.append(ele)
print("The array is: ", a)

k = minimum(a)
g = maximum(a)
print("The minimum number of the array: ", k)
print("The maximum number of the array: ", g)'''


lst = [7,5,3,1,9,6,8,4,2]
m = lst[0]
index = lst[1]
while index < len(lst):
    if index < m:
        m = index
    index = index + 1
print("The minimum number is: ", m)



'''tuple1 = (1,2,3)
tuple2 = tuple1 * 2
print(tuple2)'''

'''tuple1 = (1,2,3)
for i in tuple1:
    print(i)

for i in range(len(tuple1)):
    print(i)'''

'''tuple = (1,2,3,4,5,"ok",1.45)
tuple2 = (3,4,5,6)
tuple1'''