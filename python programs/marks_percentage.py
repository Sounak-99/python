x=[]

c=0
for i in range(5):
    n=eval(input("Enter the subject marks: "))
    x.append(n)
    c+=x[i]

percentage=(c/500)*100

print("\nPercentage = ",percentage)
if percentage >= 90 and percentage <= 100:
    print("Grade: A")
elif percentage >= 80 and percentage <= 90:
    print("Grade: B")
elif percentage >= 60 and percentage <= 70:
    print("Grade: C")
elif percentage >= 50 and percentage <= 60:
    print("Grade: D")
elif percentage >= 40 and percentage <= 50:
    print("Grade: D")
else:
    print("Grade: F")