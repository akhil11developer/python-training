"""
Write a Python program to calculate the area of a trapezoid
"""

#parellel sides of the trapezoid:
Base1 = float(input('Enter the First Base of a Trapezoid: '))
Base2 = float(input('Enter the Second Base of a Trapezoid: '))
#distance between  two parelle sides
Height= float(input('Enter the Height of a Trapezoid'))

# calculate the area of trapezoid
area = 0.5 * (Base1 + Base2) * Height

print("The Area of a trapezoid ",area)