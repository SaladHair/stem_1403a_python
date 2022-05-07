"""
pro plotter test
"""


import plotter


if __name__ == '__main__':
    plotter_instance = plotter.Plotter()
    twodshapes = []
    threedshapes = []
    parallelogram = plotter_instance.pen.drawShape("Parallelogram", 5, 10, 15)
    rectangle = plotter_instance.pen.drawShape("Rectangle", 6, 8)
    square = plotter_instance.pen.drawShape("Square", 9)
    rhombus = plotter_instance.pen.drawShape("Rhombus", 6, 8, 11)
    circle = plotter_instance.pen.drawShape("Circle", 6)
    oval = plotter_instance.pen.drawShape("Oval", 6, 8)
    triangle = plotter_instance.pen.drawShape("Triangle", 6, 8, 10, 12)
    rightTriangle = plotter_instance.pen.drawShape("RightTriangle", 3, 4, 5)
    sphere = plotter_instance.pen.drawShape("Sphere", 6)
    cube = plotter_instance.pen.drawShape("Cube", 6)
    pyramid = plotter_instance.pen.drawShape("Pyramid", 8, 4, 5.65685424949, 4, 4)
    cylinder = plotter_instance.pen.drawShape("Cylinder", 6, 8)

    for i in plotter_instance.twodshapes:
        print(f"shape {i.__str__()} has a perimeter of {plotter_instance.getPerimeter(i)} and an area of {plotter_instance.getArea(i)}")
        print(f"shape {i.__str__()} is of color {i.color}")
        plotter_instance.colorer.fillColor(i, "blue")
        print(f"shape {i.__str__()} is now of color {i.color}")

    for i in plotter_instance.threedshapes:
        print(f"shape {i.__str__()} has a perimeter of {plotter_instance.getArea(i)} and an area of {plotter_instance.getVolume(i)}")
        print(f"shape {i.__str__()} is of color {i.color}")
        plotter_instance.colorer.fillColor(i, "blue")
        print(f"shape {i.__str__()} is now of color {i.color}")
