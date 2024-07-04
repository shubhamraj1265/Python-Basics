print("************ AREA CALCULATOR **************")
print("""Press 1 to get the area of Square
Press 2 to get the area of Rectangle
Press 3 to get the area of Circle
Press 4 to get the area of Triangle""")

choice = int(input("Enter a number between 1 - 4: "))

if choice == 1:
    side = float(input("Enter the length of one side: "))
    area = side ** 2
    print("Area of Square = ", area)
elif choice == 2:
    length = float(input("Enter the length of rectangle: "))
    width = float(input("Enter the width of rectangle: "))
    area = length * width
    print("Area of Rectangle = ", area)
elif choice == 3:
    radius = float(input("Enter the radius of circle: "))
    area = ((22 / 7) * radius ** 2)
    print("Area of Circle = ", area)
elif choice == 4:
    base = float(input("Enter the base of triangle: "))
    height = float(input("Enter the height of triangle: "))
    area = 0.5 * base * height
    print("Area of Triangle = ", area)
else:
    print("Invalid Input, Please try again")
