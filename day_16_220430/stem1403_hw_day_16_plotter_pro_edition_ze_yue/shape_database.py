"""
pro plotter shape database
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


class Parallelogram(TwoDShape):
    def __init__(self, length, width, height, color=None):
        super().__init__("Parallelogram", color)
        self.length = length
        self.width = width
        self.height = height

    def getPerimeter(self):
        return self.length * 2 + self.width * 2

    def getArea(self):
        return self.length * self.height


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


class Rhombus(TwoDShape):
    def __init__(self, side_length, width, height, color=None):
        super().__init__("Rhombus", color)
        self.side_length = side_length
        self.width = width
        self.height = height

    def getPerimeter(self):
        return self.side_length * 4

    def getArea(self):
        return self.height * self.width / 2


class Circle(TwoDShape):
    def __init__(self, radius, color=None):
        super().__init__("Circle", color)
        self.radius = radius

    def getPerimeter(self):
        return self.radius * 2 * PI

    def getArea(self):
        return self.radius ** 2 * PI


class Oval(TwoDShape):
    def __init__(self, big_radius, small_radius, color=None):
        super().__init__("Oval", color)
        self.big_radius = big_radius
        self.small_radius = small_radius

    def getPerimeter(self):
        big_radius = self.big_radius
        small_radius = self.small_radius
        h = (big_radius - small_radius) ** 2 / (big_radius - small_radius) ** 2
        perimeter = PI * (big_radius + small_radius) * (
                    1 + h * 0.25 + (h ** 2) * (1 / 64) + (h ** 3) * (1 / 256) + (h ** 4) *
                    (25 / 16384) + (h ** 5) * (49 / 65536) + (h ** 6) * (441 / 1048576))
        return perimeter

    def getArea(self):
        area = PI * self.big_radius * self.small_radius
        return area


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


class RightTriangle(Triangle):
    def __init__(self, base, side, hypotenuse, color=None):
        super().__init__(base, side, hypotenuse, side, "RightTriangle", color)


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


class Pyramid(ThreeDShape):
    def __init__(self, base_side_length, base_apothem, apothem, height, side_num, color=None):
        super().__init__("Pyramid", color)
        self.base_side_length = base_side_length
        self.base_apothem = base_apothem
        self.apothem = apothem
        self.height = height
        self.side_num = side_num

    def getArea(self):
        return self.base_side_length * self.base_apothem * self.side_num / 2 + self.base_side_length * self.side_num \
               * self.height / 2

    def getVolume(self):
        return self.base_side_length * self.base_apothem * self.side_num / 2 * self.height / 3


class Cylinder(ThreeDShape):
    def __init__(self, radius, height, color=None):
        super().__init__("Cylinder", color)
        self.radius = radius
        self.height = height

    def getArea(self):
        return 2 * self.radius ** 2 * PI + self.radius * 2 * PI * self.height

    def getVolume(self):
        return self.radius ** 2 * PI * self.height
