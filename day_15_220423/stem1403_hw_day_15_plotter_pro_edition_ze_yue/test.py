import plotter


twodshapes = []
threedshapes = []
parallelogram = plotter.shape_database.Parallelogram(5, 10, 15)
twodshapes.append(parallelogram)
rectangle = plotter.shape_database.Rectangle(6, 8)
twodshapes.append(rectangle)
square = plotter.shape_database.Square(9)
twodshapes.append(square)
rhombus = plotter.shape_database.Rhombus(6, 8, 11)
twodshapes.append(rhombus)
circle = plotter.shape_database.Circle(6)
twodshapes.append(circle)
oval = plotter.shape_database.Oval(6, 8)
twodshapes.append(oval)
triangle = plotter.shape_database.Triangle(6, 8, 10, 12)
twodshapes.append(triangle)
rightTriangle = plotter.shape_database.RightTriangle(3, 4, 5)
twodshapes.append(rightTriangle)
sphere = plotter.shape_database.Sphere(6)
threedshapes.append(sphere)
cube = plotter.shape_database.Cube(6)
threedshapes.append(cube)
pyramid = plotter.shape_database.Pyramid(8, 4, 5.65685424949, 4, 4)
threedshapes.append(pyramid)
cylinder = plotter.shape_database.Cylinder(6, 8)
threedshapes.append(cylinder)

for i in twodshapes:
    print(f"shape {i.__str__()} has a perimeter of {i.getPerimeter()} and an area of {i.getArea()}")
    print(f"shape {i.__str__()} is of color {i.color}")
    plotter.Plotter.fillColor(plotter.Plotter(), i, "blue")
    print(f"shape {i.__str__()} is now of color {i.color}")

for i in threedshapes:
    print(f"shape {i.__str__()} has a volume of {i.getVolume()} and an area of {i.getArea()}")
    print(f"shape {i.__str__()} is of color {i.color}")
    plotter.Plotter.fillColor(plotter.Plotter(), i, "blue")
    print(f"shape {i.__str__()} is now of color {i.color}")
