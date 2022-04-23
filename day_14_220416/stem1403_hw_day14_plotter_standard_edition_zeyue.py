"""
[Homework]
Date: 2022-04-16
Due date: 2022-04-22
1. Project practice
Continue to finish developing a plotting application.
Implementing your first edition according to your class diagram
Revising your class diagram if necessary
Submit your code to slack
Refine or revise your system design, submit your new class diagram
"""

# Standard edition
import math

PI = math.pi


class Shape:
    def getArea(self):
        return None


class TwoDShape(Shape):
    def getPerimeter(self):
        return None


class ThreeDShape(Shape):
    def getVolume(self):
        return None


class Rectangle(TwoDShape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def getPerimeter(self):
        return self.length * 2 + self.width * 2

    def getArea(self):
        return self.length * self.width


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


class Circle(TwoDShape):
    def __init__(self, radius):
        self.radius = radius

    def getPerimeter(self):
        return self.radius * 2 * PI

    def getArea(self):
        return self.radius ^ 2 * PI


class Triangle(TwoDShape):
    def __init__(self, base, side_2, side_3, height):
        self.base = base
        self.side_2 = side_2
        self.side_3 = side_3
        self.height = height

    def getPerimeter(self):
        return self.base + self.side_2 + self.side_3

    def getArea(self):
        return self.base * self.height / 2


class Sphere(ThreeDShape):
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return 4 * PI * self.radius * 2

    def getVolume(self):
        return 4 / 3 * PI * self.radius ^ 3


class Cube(ThreeDShape):
    def __init__(self, length):
        self.length = length

    def getArea(self):
        return 6 * self.length ^ 2

    def getVolume(self):
        return self.length ^ 3


class Plotter:
    def getPerimeter(self, shape):
        return shape.getPerimeter()

    def getArea(self, shape):
        return shape.getArea()

    def getVolume(self, shape):
        return shape.getVolume()
