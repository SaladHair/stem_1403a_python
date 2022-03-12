"""
case 3. accessing methods of parent class

Parent (name, talk())
Child (name, talk())

main program/app

"""


class Parent:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("the parent talked")

    def talk3(self):
        self.talk()


class Child(Parent):
    def talk(self):
        super().talk()
        print("the child talked")

    def talk2(self):
        super().talk()


# main program
child = Child("Nolan")
print(child.name)
child.talk()
child.talk2()
child.talk3()