n = int(input("Enter the element "))

reverse = 0

while n > 0:
    r = n % 10
    reverse = reverse * 10 + r
    n = n // 10


print("The reverse number is: ", reverse)
