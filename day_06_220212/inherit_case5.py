"""
case 4. defining __init__ method in child class

Parent (name, __talk())
Child (name, talk())

main program/app

"""


class Parent:
    def __init__(self, name):
        self.name = name

    # def __talk(self):
    #     print("the parent talked")


class Child(Parent):
    def __init__(self):
        pass
    # def talk(self):
    #     super()._Parent__talk()
    #     super()._Parent__name = "Roger 2"


# main program
child = Child()
print(child.name)
