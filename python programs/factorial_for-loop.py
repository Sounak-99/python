'''def factorial_for_loop(n):
    fact = 1
    for i in range(1,n+1):
       fact = fact * i
    return fact


def factoial_while_loop(x):
    fact = 1
    while x > 0:
        fact = fact * x
        x = x - 1
    return fact

n = int(input("Enter the input: "))
k = factorial_for_loop(n)
print("Result of factorial_for_loop: ", k)
b = factoial_while_loop(n)
print("Result of factorial_while_loop: ", b)'''


def sum_factorial(n):
    fact = 1
    sum = 0
    for i in range(1, n+1):
        fact = fact * i
        sum = sum + fact
        if i == n:
            print(i,'!:-', sum)
        else:
            print(i, end="! + ")


n = int(input("Enter the input: "))
sum_factorial(n)



