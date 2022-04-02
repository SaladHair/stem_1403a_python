"""
[Homework]
Date: 2022-03-26
Due date: 2022-04-01
1. Rewriting the program
Set Canadian taxes for your online store
Consider a scenario that Peter, Mary, Jack want to open online stores in Canada.
Peter chooses the consumers from BC.
Mary chooses the consumers from QC.
Jack chooses the consumers from ON.
Please write a program to determine the taxes for their online stores.
Please write the main logic as well for the test.
Hints:
Design class diagram
Applying polymorphism to the implementation
"""

GST = 0.05
PST = 0.07
QST = 0.09975
HST = 0.13


class Customer:
    def __init__(self, order_cost, region):
        self.order_cost = order_cost
        self.region = region

    def calc_price(self):
        if self.region == "BC":
            return BCStore.calc_price(BCStore(), self.order_cost)
        elif self.region == "QC":
            return QCStore.calc_price(QCStore(), self.order_cost)
        else:
            return ONStore.calc_price(ONStore(), self.order_cost)


class Store:

    def calc_price(self, order_price):
        return order_price


class BCStore(Store):

    def calc_price(self, order_price):
        return order_price * (1+GST+PST)


class QCStore(Store):

    def calc_price(self, order_price):
        return order_price * (1+GST+QST)


class ONStore(Store):

    def calc_price(self, order_price):
        return order_price * (1+HST)


john = Customer(500, "BC")
print(f"John's order cost {john.order_cost}$ before taxes and {round(john.calc_price(), 2)}$ after taxes.")
matthew = Customer(700, "QC")
print(f"Matthew's order cost {matthew.order_cost}$ before taxes and {round(matthew.calc_price(), 2)}$ after taxes.")
martin = Customer(650, "ON")
print(f"Martin's order cost {martin.order_cost}$ before taxes and {round(martin.calc_price(), 2)}$ after taxes.")