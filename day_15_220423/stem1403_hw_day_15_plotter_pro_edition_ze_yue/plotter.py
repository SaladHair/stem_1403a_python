"""
[Homework]
Date: 2022-04-23
Due date: 2022-04-29
1. Project practice
Continue to finish developing a plotting application.
Implementing your 2nd edition according to your class diagram
Implementing your 1st edition according to your class diagram if necessary
"""

import shape_database
import math

PI = math.pi


class Plotter:
    def getPerimeter(self, shape):
        return shape.getPerimeter()

    def getArea(self, shape):
        return shape.getArea()

    def getVolume(self, shape):
        return shape.getVolume()

    def fillColor(self, shape, color):
        shape.color = color
