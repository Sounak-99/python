def compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100)**time
    ci = amount - principal
    return ci



x = int(input("Enter the Principal: "))
y = int(input("Enter the rate of interest: "))
z = int(input("Enter the time: "))
k = compound_interest(x, y, z)
print("The compund interest is: ", k)