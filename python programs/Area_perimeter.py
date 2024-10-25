def rectangle_area(length, breadth):
    area = length * breadth
    return area


def rectangle_perimeter(length, breadth):
    perimeter = 2 * (length + breadth)
    return perimeter


x = int(input("Enter the Length of the rectangle: "))
y = int(input("Enter the Breadth of the rectangle: "))
k = rectangle_area(x,y)
z = rectangle_perimeter(x,y)
print("The are of the rectangle: ", k)
print("The perimeter of the rectangle: ", z)
