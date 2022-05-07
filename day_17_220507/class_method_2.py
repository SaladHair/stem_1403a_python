"""
class method

project : order system
"""


class Order:

    currentOrderID = 0

    @classmethod
    def getNextOrderID(cls):
        nextOrderID = cls.currentOrderID + 1
        cls.currentOrderID = nextOrderID
        return nextOrderID


# test
print(Order.getNextOrderID())
print(Order.getNextOrderID())
print(Order.getNextOrderID())
print(Order.getNextOrderID())
print(Order.getNextOrderID())