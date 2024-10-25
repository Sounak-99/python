'''a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
temp = 0
print("Before swap the value of a: ", a)
print("Before swap the value of b: ", b)
temp = a
a = b
b = temp
print("After swap the value of a: ", a)
print("After swap the value of b: ", b)'''




'''a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
temp = 0
print("Before swap the value of a: ", a)
print("Before swap the value of b: ", b)
a = a + b
b = a - b
a = a - b
print("After swap the value of a: ", a)
print("After swap the value of b: ", b)'''

#area = pi*r*r
#curmstance = 2*pi*r

'''def area(n):
    print("Area of the circle:- ", 3.14*n**2)

def circum(n):
    print("The radius of a circle:- ", 2*3.14*n)

radius = int(input("Enter the radius: "))
area(radius)
circum(radius)'''

#ci = p*(1+r/100)**t
'''def simple_interest(p,r,t):
    si = (p*r*t)/100
    amount = p + si
    return si,amount

p = int(input("Enter the principal amaount: "))
r = int(input("Enter the rate of interest: "))
t = int(input("Enter the time: "))
i,a = simple_interest(p,r,t)
print("Interest: ", i)
print("Amount is: ", a)'''

'''list = [7,5,3,1,9,6,8,4,2]
maximum = max(list)
minimum = min(list)
print("The maximum number is: ", maximum)
print("The minimum number is: ", minimum)'''

'''def maximum(list):
    index = 1
    ma = list[0]
    while index < len(list):
        if list[index] > ma:
            ma = list[index]
        index += 1
    return ma


def minimum(list):
    index = 1
    mi = list[0]
    while index < len(list):
        if list[index] < mi:
            mi = list[index]
        index += 1
    return mi



list = [7,5,3,1,9,6,8,4,2]
maxi = maximum(list)
mini = minimum(list)
print("The minimum number: ", mini)
print("The maximum number: ", maxi)'''


'''def fibo(count):
    num1 = 0
    num2 = 1
    if count < 1:
        print("count should be > 0")
    elif count == 1:
        print(num1)
    elif count == 2:
        print(num1,num2)
    else:
        print(num1, num2, end=" ")
        count = count - 2
        while count > 0:
            next = num1 + num2
            print(next, end=" ")
            num1 = num2
            num2 = next
            count -= 1



count = int(input("Enter a number: "))
fibo(count)'''


   '''p = int(input("Enter the power: "))
    k = int(input("Enter the input: "))
    c = k
    result = 0
    arm = 0
    while k > 0:
        r = k % 10
        arm = arm + r**p
        k = k // 10


    if result == arm:
        print("The number is armstrong number: ", arm)
    else:
        print("The number is not armstrong: ", arm)'''


'''nested_list = [1,[2,3],[4,[5,6]]]
print(nested_list)
print(nested_list[0])
print(nested_list[1][1])
print(nested_list[1])
print(nested_list[2])
print(nested_list[2][1])
print(nested_list[2][0])
print(nested_list[0][1])'''


'''my_tuple = (1,2,3)
my_list = list(my_tuple)
print(my_list)'''




