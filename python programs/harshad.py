x = int(input("Enter the number: "))
quotiend = 0
p = x

while x > 0:
    r = x % 10
    quotiend = quotiend * 1 + r
    x = x // 10
print("The sum of its digit: ", quotiend)

if p % quotiend == 0:
    print("the number is harshad number: ", quotiend)
else:
    print("The number is not harshad number: ", quotiend)