#find unique element from the list

'''def unique_list(list):
    result = []
    for item in list:
        if item not in result:
            result.append(item)
    return result


lst = [1,2,3,2,5,3,1,9]
print(unique_list(lst))'''

#count the number of vowels:

'''def vowel_count(str):
    count = 0
    vowel = list("aeiouAEIOU")
    for alphabet in str:
        if alphabet in vowel:
            count = count + 1
    return count

str = "The Quick Brown Fox Jumps Over The Lazy Frog"
print("No of vowel in given string is: ", vowel_count(str))'''

#BMI calculate

def BMI_calculater(weight, height):
    return weight/(height/100)**2


'''def BMI_scale(weight, height):
    index = BMI_calculater(weight,height)
    if index < 18.5:
        print("The persion is under weight")
    elif index < 24.9:
       print("The person is Under Healthy")
    elif index < 30:
        print("The person is over weight")
    else:
        print("The person is Obsesity")



weight = float(input("Enter your Weight(kg): "))
height = float(input("Enter your height(cm): "))

BMI_scale(weight, height)'''

#Example of set in python
'''my_set = {1,2,3,4,4,5,5,6}
print(my_set) #doesn't allow duplicate element in a set

my_set.add(7) #add an element at the end of the set
print(my_set)

my_set.remove(1) #removes an element from the set
print(my_set)

print(2 in my_set) #if the value is present in the set then it will return true as output'''

#Example of dictionary in python
'''my_dict = {'name': 'sounak', 'age': 19, 'city': 'Kolkata'}
print(my_dict['name']) #accesing a value from dict by its key
my_dict['job'] = 'Coding' #adding a new key-value pair
print(my_dict)
del my_dict['age'] #removing a key-value from dict
print(my_dict)'''

#empty dict
'''my_dict = {} # can create by curly brases
my_dict = dict() # can create by parantheases

my_dict['value'] = 25
print(my_dict)'''


'''import turtle

# Set up screen
screen = turtle.Screen()
screen.title("Dick Shape")

# Create turtle object
dick = turtle.Turtle()
dick.speed(2)  # Set drawing speed

# Draw shaft
dick.fillcolor("blue")
dick.begin_fill()
dick.forward(100)  # Length of shaft
dick.circle(20, 180)  # Curve at end
dick.forward(100)
dick.end_fill()

# Draw head
dick.penup()
dick.goto(0, 100)  # Move to head position
dick.pendown()
dick.fillcolor("red")
dick.begin_fill()
dick.circle(20)  # Head
dick.end_fill()

# Hide turtle object
dick.hideturtle()

# Keep window open
turtle.done()'''


'''add = lambda x,y:x+y
store = add(3,5)
print("The result is: ", store)'''

'''square = lambda x: x*x
print(square(4))'''

'''number = [1,2,3,4,5]
double = map(lambda x:x*2, number)
print(list(double))'''

'''math_module.py'''
'''def add(a,b):
    return a + b

import math

result = math_module.add(3,5) #this gonna add the two numbers
print(result) #And the output will be 8'''




import math_module

result = math_module.add(3, 5)
print(result)  # Output: 8


    
