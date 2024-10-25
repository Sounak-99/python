def maximum(list):
    max = list[0]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
            i = i + 1
    return max

def minimum(list):
    min = list[0]
    for i in range(len(list)):
        if list[i] < min:
            min = list[i]
            i = i + 1
    return min

list = []
n = int(input("Enter the range: "))
for i in range(0,n):
    x = int(input("Enter the elements: "))
    list.append(x)
print("The list is: ", list)

k = maximum(list)
g = minimum(list)
print("The maximum number is: ", k)
print("The minimum number is: ", g)
