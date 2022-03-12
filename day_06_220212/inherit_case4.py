"""
case 4. forcely accessing private properties and methods of parent class

Parent (name, __talk())
Child (name, talk())

main program/app

"""


class Parent:
    def __init__(self, name):
        self.__name = name

    def __talk(self):
        print("the parent talked")



class Child(Parent):
    def talk(self):
        super()._Parent__talk()
        # super()._Parent__name = "Roger 2"


# main program
child = Child("Nolan")
# print(child.name)
# print(child._Parent__name)
child.talk()
