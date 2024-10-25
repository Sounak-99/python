n = int(input("Enter the range of the tuple: "))
x = []
for i in range(n):
    number = int(input("Enter the eliments of the tuple: "))
    cube = number ** 3
    x.append((number,cube))

print("The cube tuple is: ", x)