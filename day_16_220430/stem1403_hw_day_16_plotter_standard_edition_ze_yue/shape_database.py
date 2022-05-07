"""
standard plotter shape database
"""


import math

PI = math.pi


class Shape:
    def __init__(self, name, color=None):
        self.name = name
        self.color = color

    def getArea(self):
        return None

    def __str__(self):
        return self.name


class TwoDShape(Shape):
    def __init__(self, name, color=None):
        super().__init__(name, color)

    def getPerimeter(self):
        return None


class ThreeDShape(Shape):
    def __init__(self, name, color=None):
        super().__init__(name, color)

    def getVolume(self):
        return None


class Rectangle(TwoDShape):
    def __init__(self, length, width, name="Rectangle", color=None):
        super().__init__(name, color)
        self.length = length
        self.width = width

    def getPerimeter(self):
        return self.length * 2 + self.width * 2

    def getArea(self):
        return self.length * self.width


class Square(Rectangle):
    def __init__(self, length, color=None):
        super().__init__(length, length, "Square", color)


class Circle(TwoDShape):
    def __init__(self, radius, color=None):
        super().__init__("Circle", color)
        self.radius = radius

    def getPerimeter(self):
        return self.radius * 2 * PI

    def getArea(self):
        return self.radius ** 2 * PI


class Triangle(TwoDShape):
    def __init__(self, base, side_2, side_3, height, name="Triangle", color=None):
        super().__init__(name, color)
        self.base = base
        self.side_2 = side_2
        self.side_3 = side_3
        self.height = height

    def getPerimeter(self):
        return self.base + self.side_2 + self.side_3

    def getArea(self):
        return self.base * self.height / 2


class Sphere(ThreeDShape):
    def __init__(self, radius, color=None):
        super().__init__("Sphere", color)
        self.radius = radius

    def getArea(self):
        return 4 * PI * self.radius * 2

    def getVolume(self):
        return 4 / 3 * PI * self.radius ** 3


class Cube(ThreeDShape):
    def __init__(self, length, color=None):
        super().__init__("Cube", color)
        self.length = length

    def getArea(self):
        return 6 * self.length ** 2

    def getVolume(self):
        return self.length ** 3
