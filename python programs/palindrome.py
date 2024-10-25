n = int(input("Enter the element: "))

c = n
reverse = 0

while n != 0:
    r = n % 10
    reverse = reverse * 10 + r
    n = n // 10
if c == reverse:
    print("The number is palindrome", reverse)
else:
    print("The number is not palindrome", reverse)
