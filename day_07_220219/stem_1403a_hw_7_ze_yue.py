"""
[Homework]
Date: 2022-02-19
Due date: 2022-02-25
1. Programming practice
Write a utility program in Java for calculating area of shapes.
Shapes are as follows:
(a) circle
(b) square
(c) equilateral triangle
Hints:
Design a parent class such as Shape
Design a method (i.e. method name could be getArea ) to calculate the area in the Shape class
Design classes for every shape
Design a method for each to calculate the area
Those methods must override the method (i.e. getArea )
Those methods have the same signature
Each method accepts one parameter of double type
Be noted that the formula can be taken as a function of x, where x is the parameter as input.
Formulas:
The area of circle:        f(r) = Pi * r * r   (where r is radius as input)
The area of square:     f(a) = a * a    (where a is side of square as input)
The area of equilateral triangle:   Heron's formula (refer to the link below)
"""

import math


class Shape:
    def getArea(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        area = self.radius ** 2 * math.pi
        return area


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def getArea(self):
        area = self.side_length ** 2
        return area


class EquilateralTriangle(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def getArea(self):
        area = self.side_length * math.sqrt(self.side_length ** 2 - (self.side_length / 2) ** 2) / 2
        return area


circle = Circle(10)
square = Square(5)
triangle = EquilateralTriangle(15)

print(circle.getArea())  # 314.1592653589793
print(square.getArea())  # 25
print(triangle.getArea())  # 97.42785792574935
