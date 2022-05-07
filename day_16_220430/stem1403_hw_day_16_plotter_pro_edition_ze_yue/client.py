"""
pro plotter client app
"""


import plotter


# plotter
plotter_instance = plotter.Plotter()

# shapes
two_d_shapes = {'1': "Parallelogram", '2': "Rectangle", '3': "Square", '4': "Rhombus", '5': "Circle", '6': "Oval", '7': "Triangle",
                '8': "RightTriangle"}
three_d_shapes = {'1': "Sphere", '2': "Cube", '3': "Pyramid", '4': "Cylinder"}

dimensions = {"Parallelogram": "Length, width, height", "Rectangle": "Length, width", "Square": "Length",
              "Rhombus": "Side length, width, height", "Circle": "Radius", "Oval": "Big radius, small radius",
              "Triangle": "Base length, second side length, third side length, height", "RightTriangle": "Base length"
                                                                                                         ", side length"
                                                                                                         ", hypotenuse",
              "Sphere": "Radius", "Cube": "Side length", "Pyramid": "Base side length, base apothem, apothem, height,"
                                                                    " number of sides", "Cylinder": "Radius, height"}

shape = "Parallelogram"

# menus:
main_menu = "To plot a shape, type '1'. To exit, type 'exit'."

plot_menu = "To plot a 2D shape, type '1'. To plot a 3D shape, type '2'. To go back to the previous menu, type 'back'."
two_d_menu = "Type the number below that corresponds to the shape you wish to plot, or 'back' to go back\n" \
             "1 : Parallelogram\n" \
             "2 : Rectangle\n" \
             "3 : Square\n" \
             "4 : Rhombus\n" \
             "5 : Circle\n" \
             "6 : Oval\n" \
             "7 : Triangle\n" \
             "8 : Right triangle"

three_d_menu = "Type the number below that corresponds to the shape you wish to plot, or 'back' to go back\n" \
             "1 : Sphere\n" \
             "2 : Cube\n" \
             "3 : Pyramid\n" \
             "4 : Cylinder" \

dimensions_menu = f"Type the dimensions of your shape separated by commas in this order, or 'back' to go back:" \



def main():
    global shape
    menu = "main"
    last_menu = None
    while menu != "exit":
        if menu == "main":
            print(main_menu)
            received_input = input()
            if received_input == "1":
                menu = "plot"
                last_menu = "main"
            elif received_input == "exit":
                menu = "exit"
        elif menu == "plot":
            print(plot_menu)
            received_input = input()
            if received_input == "1":
                menu = "2d"
                last_menu = "plot"
            elif received_input == "2":
                menu = "3d"
                last_menu = "plot"
            elif received_input == "back":
                menu = last_menu
        elif menu == "2d":
            print(two_d_menu)
            received_input = input()
            if received_input == "back":
                menu = last_menu
            elif received_input in two_d_shapes:
                shape = two_d_shapes[received_input]
                menu = "dimensions"
                last_menu = "2d"

        elif menu == "3d":
            print(three_d_menu)
            received_input = input()
            if received_input == "back":
                menu = last_menu
            elif received_input in three_d_shapes:
                shape = three_d_shapes[received_input]
                menu = "dimensions"
                last_menu = "3d"

        elif menu == "dimensions":
            print(dimensions_menu)
            print(f"{dimensions[shape]}")
            received_input = input()
            if received_input == "back":
                menu = last_menu
            else:
                received_input = received_input.split(",")
                received_input = [int(x) for x in received_input]
                plotter_instance.pen.drawShape(shape, *received_input)
                if last_menu == "2d":
                    print(
                        f"shape {plotter_instance.twodshapes[-1]} has a perimeter of "
                        f"{plotter_instance.getPerimeter(plotter_instance.twodshapes[-1])} and an area of "
                        f"{plotter_instance.getArea(plotter_instance.twodshapes[-1])}")
                    print("Type 1 if you would like to add a color to the shape, or 'back' to go back to the main menu")
                    received_input = input()
                    if received_input == "back":
                        menu = "main"
                    elif received_input == "1":
                        print("Type the color you wish to fill the shape with, or 'back' to go back to the main menu")
                        received_input = input()
                        if received_input == "back":
                            menu = "main"
                        else:
                            plotter_instance.colorer.fillColor(plotter_instance.twodshapes[-1], received_input)
                            print(f"shape {plotter_instance.twodshapes[-1].__str__()} is now of color "
                                  f"{plotter_instance.twodshapes[-1].color}")

                elif last_menu == "3d":
                    print(
                        f"shape {plotter_instance.threedshapes[-1]} has a perimeter of "
                        f"{plotter_instance.getArea(plotter_instance.threedshapes[-1])} and an area of "
                        f"{plotter_instance.getVolume(plotter_instance.threedshapes[-1])}")
                    print("Type 1 if you would like to add a color to the shape, or 'back' to go back to the main menu")
                    received_input = input()
                    if received_input == "back":
                        menu = "main"
                    elif received_input == "1":
                        print("Type the color you wish to fill the shape with, or 'back' to go back to the main menu")
                        received_input = input()
                        if received_input == "back":
                            menu = "main"
                        else:
                            plotter_instance.colorer.fillColor(plotter_instance.threedshapes[-1], received_input)
                            print(f"shape {plotter_instance.threedshapes[-1].__str__()} is now of color "
                                  f"{plotter_instance.threedshapes[-1].color}")

                else:
                    print("An error has occurred, going back to main menu")

                menu = "main"

    print("Program terminated")


# main program
if __name__ == "__main__":
    main()
