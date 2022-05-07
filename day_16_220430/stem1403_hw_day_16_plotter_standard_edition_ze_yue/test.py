"""
standard plotter test
"""


import plotter


if __name__ == '__main__':
    plotter_instance = plotter.Plotter()
    twodshapes = []
    threedshapes = []
    rectangle = plotter_instance.pen.drawShape("Rectangle", 6, 8)
    square = plotter_instance.pen.drawShape("Square", 9)
    circle = plotter_instance.pen.drawShape("Circle", 6)
    triangle = plotter_instance.pen.drawShape("Triangle", 6, 8, 10, 12)
    sphere = plotter_instance.pen.drawShape("Sphere", 6)
    cube = plotter_instance.pen.drawShape("Cube", 6)

    for i in plotter_instance.twodshapes:
        print(f"shape {i.__str__()} has a perimeter of {plotter_instance.getPerimeter(i)} and an area of {plotter_instance.getArea(i)}")


    for i in plotter_instance.threedshapes:
        print(f"shape {i.__str__()} has a perimeter of {plotter_instance.getArea(i)} and an area of {plotter_instance.getVolume(i)}")
