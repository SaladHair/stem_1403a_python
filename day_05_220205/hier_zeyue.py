"""
Inheritance type :  hierarchical inheritance
Description:
Weapon (length, weight, one_handed, attack())
Bow (curve_strength, string_length, arrow_type, fire_arrow())
Spear (tip_length, diameter, spin(), stab())
A bow is a type of weapon.
A spear is a type of weapon.

"""


class Weapon:
    def __init__(self, length, weight, one_handed):
        self.length = length
        self.weight = weight
        self.one_handed = one_handed

    def attack(self):
        print("the weapon is attacking")


class Bow(Weapon):
    def __init__(self, length, weight, one_handed, curve_strength, string_length, arrow_type):
        super().__init__(length, weight, one_handed)
        self.curve_strength = curve_strength
        self.string_length = string_length
        self.arrow_type = arrow_type

    def fire_arrow(self):
        print("the bow fired an arrow")


class Spear(Weapon):
    def __init__(self, length, weight, one_handed, tip_length, diameter):
        super().__init__(length, weight, one_handed)
        self.tip_length = tip_length
        self.diameter = diameter

    def spin(self):
        print("the spear spun")

    def stab(self):
        print("the spear moved forward")


# main program
weapon = Weapon("0,5 meters", "15kg", "yes")
print(weapon.length, weapon.weight, weapon.one_handed)
weapon.attack()

bow = Bow("0,5 meters", "10 kg", "no", "45 degrees", "0,45 meters", "plain arrow")
print(bow.length, bow.weight, bow.one_handed, bow.curve_strength, bow.string_length, bow.arrow_type)
bow.attack()
bow.fire_arrow()

spear = Spear("1,6 meters", "20 kg", "no", "0,3 meters", "0,1 meter")
print(spear.length, spear.weight, spear.one_handed, spear.tip_length, spear.diameter)
spear.attack()
spear.spin()
spear.stab()
