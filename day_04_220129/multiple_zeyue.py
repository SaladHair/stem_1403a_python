"""
Inheritance type :  hierarchical inheritance
Description:
Tiger (height, width, run(), rest(), growl())
Lion (height, width, run(), rest(), growl())
Liger (fur_color, roar())
A Liger is a combination of a lion and a tiger.

# Modifications

"""

class Tiger:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def run(self):
        print("the tiger is running")

    def rest(self):
        print("the tiger is resting")

    def growl(self):
        print("the tiger is growling")


class Lion:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def run(self):
        print("the lion is running")

    def rest(self):
        print("the lion is resting")

    def growl(self):
        print("the lion is growling")


class Liger(Tiger, Lion):
    def __init__(self, height, width, fur_color):
        super().__init__(height, width)
        self.fur_color = fur_color

    def roar(self):
        print("the liger roared")


# main program
tiger = Tiger("0,5 meters", "1 meter")
print(tiger.height, tiger.width)
tiger.run()
tiger.rest()
tiger.growl()

lion = Lion("0,5 meters", "1 meter")
print(lion.height, lion.width)
lion.run()
lion.rest()
lion.growl()

liger = Liger("0,5 meters", "1 meter", "Orange")
print(liger.height, liger.width, liger.fur_color)
liger.roar()
