n = int(input("Enter the input: "))

remainder = 0
c = n

while n > 0:
    r = n % 10
    remainder = remainder + (r*r*r)
    n = n // 10

if c == remainder:
    print("The number is armstrong", remainder)
else:
    print("The number is not armstrong", remainder)
