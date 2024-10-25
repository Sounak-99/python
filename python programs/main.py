'''print("hello world")'''

'''import math_module

result = math_module.add(3, 5)
print(result)  # Output: 8'''

'''import math_module'''

'''x = int(input("Enter the first input: "))
y = int(input("Enter the second input: "))
result = math_module.add(x,y)
print("The final result is: ", result)'''

'''n = int(input("Enter the input: "))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print("The factorial is: ", fact)'''

'''n = int(input("Enter The input: "))
fact = 1
while n > 0:
    fact = fact * n
    n = n - 1
print("THe factorial is: ", fact)'''

'''def facto(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print("The factorial using for loop: ", fact)


def facto2(n):
    fact = 1
    while n > 0:
        fact = fact * n
        n = n - 1
    print("The factorial using while loop: ", fact)


def facto3(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact


def facto4(n):
    fact = 1
    while n > 0:
        fact = fact * n
        n = n - 1
    return fact



x = int(input("Enter the input: "))
facto(x)
facto2(x)
k = facto3(x)
y = facto4(x)
print("The return type for loop factorial: ", k)
print("The return type while loop factorial is: ", y)'''


'''n = int(input("Enter the input: "))
reverse = 0
while n > 0:
    r = n % 10
    reverse = reverse * 10 + r
    n = n // 10

print("THe reverse number is: ", reverse)'''

'''n = int(input("Enter the input: "))
k = n
reverse = 0

while n > 0:
    r = n % 10
    reverse = reverse * 10 + r
    n = n // 10

if k == reverse:
    print("The number is palindrome: ", reverse)
else:
    print("The number is not palindrome: ", reverse)'''


'''n = int(input("Enter the input: "))
k = n
arm = 0

while n > 0:
    r = n % 10
    arm = arm + (r*r*r)
    n = n // 10


if k == arm:
    print("The number is armstrong: ", arm)
else:
    print("The number is not armstrong: ", arm)'''

'''n = int(input("Enter the input: "))
count = 0
for i in range(1 , n+1):
    if n % i == 0:
      print("The prime factors are: ", i)
      count = count + 1


if count == 2:
    print("The number is prime: ", n)
else:
    print("The number is not prime: ", n)'''

'''n = int(input("Enter the input: "))
count = 0

for i in range(1, n+1):
    if n % i == 0:
      print("The factors are: ", i);'''

'''n = int(input("Enter the input: "))
sum = 0
for i in range(1,n):
    if n % i == 0:
         sum = sum + i


if sum == n:
    print("The number is perfect: ", sum)
else:
    print("The number is not perfect: ", sum)'''

'''n = int(input("Enter the input: "))

a = 0
b = 1

print("Fibanocci series: ")

for i in range(n):
    print(a, end=" ")
    next = a + b
    a = b
    b = next'''

'''def facto(n):
    if n == 0:
        return 1
    else:
        return n * facto(n-1)


x = int(input("Enter the input: "))
k = facto(x)
print("The recursion factorial is: ", k)'''

string1 = input("Enter the 1st string: ")
string2 = input("Enter the 2nd string: ")
result = string1+ " " +string2
print("The final string is: ", result)




