"""
Hybrid Inheritance
"""


class Car:
    def accelerate(self):
        print("The car accelerated")

    def brake(self):
        print("The car braked")

    def turn(self):
        print("The car turned")


class ElectricCar(Car):
    def recharge(self):
        print("The electric car recharged")


class FuelCar(Car):
    def refill(self):
        print("The fuel car refilled")


class HybridCar(ElectricCar, FuelCar):
    def switchMode(self):
        print("The hybrid car switched mode")