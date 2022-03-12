"""
Inheritance type :  hierarchical inheritance
Description:
Animal (height, width, weight, move(), rest())
Tiger (run(), growl())
Lion (run(), growl())
Ligre (fur_color, roar())
A ligre is a combination of a lion and a tiger, which are both mammals.

# Modifications

"""


class Animal:
    def __init__(self, num_of_legs, height, width, weight):
        self.num_of_legs = num_of_legs
        self.height = height
        self.width = width
        self.weight = weight

    def move(self):
        print("the animal is moving")

    def rest(self):
        print("the animal is resting")


class Tiger(Animal):
    def __init__(self, num_of_legs, height, width, weight):
        super().__init__(num_of_legs, height, width, weight)

    def run(self):
        print("the tiger is running")

    def growl(self):
        print("the tiger is growling")


class Lion(Animal):
    def __init__(self, num_of_legs, height, width, weight):
        super().__init__(num_of_legs, height, width, weight)

    def run(self):
        print("the lion is running")

    def growl(self):
        print("the lion is growling")


class Liger(Tiger, Lion):
    def __init__(self, num_of_legs, height, width, weight, fur_color):
        super().__init__(num_of_legs, height, width, weight)
        self.fur_color = fur_color

    def roar(self):
        print("the liger roared")


# main program
animal = Animal(4, "0,5 meters", "1 meter", "300kg")
print(animal.num_of_legs, animal.height, animal.width)
animal.move()
animal.rest()

tiger = Tiger(4, "0,5 meters", "1 meter", "200kg")
print((tiger.num_of_legs, tiger.height, tiger.width, tiger.weight))
tiger.run()
tiger.rest()
tiger.growl()

lion = Lion(4, "0,5 meters", "1 meter", "190kg")
print((lion.num_of_legs, lion.height, lion.width, lion.weight))
lion.run()
lion.rest()
lion.growl()

liger = Liger(4, "0,5 meters", "1 meter", "190kg", "Orange")
print(liger.height, liger.width, liger.fur_color)
liger.roar()
