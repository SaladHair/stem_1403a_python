"""
standard plotter plotter
"""

from shape_database import *
import math
import time

PI = math.pi


class Plotter:
    def __init__(self):
        self.twodshapes = []
        self.threedshapes = []
        self.pen = Pen(self)

    def getPerimeter(self, shape):
        return shape.getPerimeter()

    def getArea(self, shape):
        return shape.getArea()

    def getVolume(self, shape):
        return shape.getVolume()


class Pen:
    def __init__(self, plotter):
        self.plotter = plotter

    def drawShape(self, shape, *dimensions):
        print(f"Drawing {shape}...")
        if issubclass(eval(shape), TwoDShape):
            self.plotter.twodshapes.append(eval(shape)(*dimensions))
        else:
            self.plotter.threedshapes.append(eval(shape)(*dimensions))

        time.sleep(1)
        print(f"Drawing {shape} completed")
