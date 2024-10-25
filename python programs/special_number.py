n = int(input("Enter the number: "))
a = n
sp = 0
while n > 0:
    d = n % 10
    c = 1
    for i in range(1,d+1):
        c = c * i
    sp = sp + c
    n = n // 10

if sp == a:
    print("The number is a special number: ", sp)
else:
    print("The number is not special number: ", sp)