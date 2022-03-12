"""
[Homework]
Date: 2022-02-26
Due date: 2022-03-04
1. Programming practice
Problem:	Set Canadian taxes for your online store
Consider a scenario that Peter, Mary, Jack want to open online stores in Canada.
Peter chooses the consumers from BC.
Mary chooses the consumers from QC.
Jack chooses the consumers from ON.
Tax Rate:
BC	GST+PST  5% + 7%
QC	GST+QST  5% + 9.975%
ON	HST            13%
Requirements:
You are asked to write a program to provide tax calculating functionalities.
Implement your design or idea by writing code
Find out entities (for classes)
Find out methods required to this business
Test code is required
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
            return BCStore.calc_price(BCStore, self.order_cost)
        elif self.region == "QC":
            return QCStore.calc_price(QCStore, self.order_cost)
        else:
            return ONStore.calc_price(ONStore, self.order_cost)


class BCStore:
    tax_rate = GST + PST

    def calc_price(self, order_price):
        return order_price * (1+self.tax_rate)


class QCStore:
    tax_rate = GST + QST

    def calc_price(self, order_price):
        return order_price * (1+self.tax_rate)


class ONStore:
    tax_rate = HST

    def calc_price(self, order_price):
        return order_price * (1+self.tax_rate)


john = Customer(500, "BC")
print(f"John's order cost {john.order_cost}$ before taxes and {round(john.calc_price(), 2)}$ after taxes.")
matthew = Customer(700, "QC")
print(f"Matthew's order cost {matthew.order_cost}$ before taxes and {round(matthew.calc_price(), 2)}$ after taxes.")
martin = Customer(650, "ON")
print(f"Martin's order cost {martin.order_cost}$ before taxes and {round(martin.calc_price(), 2)}$ after taxes.")