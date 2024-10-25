def facto(n):
    sum = 0
    fact = 1
    for i in range(1,n+1):
      fact = fact * i
      sum = sum + fact
    return sum

def sum_series(n):
    for i in range(1,n+1):
        if i == n:
            print(i,"!", end=" ")
        else:
            print(i,"! +", end=" ")

n = int(input("Enter the number: "))
s = facto(n)
k = sum_series(n)
print(":- ", s)