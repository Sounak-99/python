def sum_list():
    list = []

    n = int(input("Enter the list Range: "))
    sum = 0
    for i in range(0, n):
        ele = int(input("Enter the list element: "))
        list.append(ele)
        sum = sum + list[i]
    print(list,":- ", sum)


sum_list()