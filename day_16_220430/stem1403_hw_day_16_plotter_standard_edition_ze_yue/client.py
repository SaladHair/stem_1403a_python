"""
standard plotter client app
"""


import plotter


# plotter
plotter_instance = plotter.Plotter()

# shapes
two_d_shapes = {'1': "Rectangle", '2': "Square", '3': "Circle", '4': "Triangle",}
three_d_shapes = {'1': "Sphere", '2': "Cube"}

dimensions = {"Rectangle": "Length, width", "Square": "Length", "Circle": "Radius", "Oval": "Big radius, small radius",
              "Triangle": "Base length, second side length, third side length, height", "Sphere": "Radius",
              "Cube": "Side length"}

shape = "Parallelogram"

# menus:
main_menu = "To plot a shape, type '1'. To exit, type 'exit'."

plot_menu = "To plot a 2D shape, type '1'. To plot a 3D shape, type '2'. To go back to the previous menu, type 'back'."
two_d_menu = "Type the number below that corresponds to the shape you wish to plot, or 'back' to go back\n" \
             "2 : Rectangle\n" \
             "3 : Square\n" \
             "5 : Circle\n" \
             "7 : Triangle\n" \

three_d_menu = "Type the number below that corresponds to the shape you wish to plot, or 'back' to go back\n" \
             "1 : Sphere\n" \
             "2 : Cube\n" \


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

                elif last_menu == "3d":
                    print(
                        f"shape {plotter_instance.threedshapes[-1]} has a perimeter of "
                        f"{plotter_instance.getArea(plotter_instance.threedshapes[-1])} and an area of "
                        f"{plotter_instance.getVolume(plotter_instance.threedshapes[-1])}")

                else:
                    print("An error has occurred, going back to main menu")

                menu = "main"

    print("Program terminated")


# main program
if __name__ == "__main__":
    main()
