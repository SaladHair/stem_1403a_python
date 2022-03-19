"""
[Homework]
Date: 2022-03-12
Due date: 2022-03-18
1. Programming practice
Problem: Bank Interest
Background:
Peter is living in a town. There are 3 banks in his town which are BankA, BankB, and BankC.
Each bank has a few branches.
He wants to know the interest rate of each bank, so that he could make a decision on which bank he is going to open a savings account at.
BankA - 0.04  (4%)
BankB - 0.0395 (3.95%)
BankC - 0.035 (3.5%)
Requirement:
Please write a small application for the residents of the town to easily check the current interest rate information of all banks at any time.
"""


class Bank:
    def __init__(self, name, interest_rate):
        self.name = name
        self.interest_rate = interest_rate

    def getInterestRate(self):
        return f"{self.name}'s interest rate is {str(self.interest_rate)} ({str(round(self.interest_rate*100, 2))}%)"


class InterestApp:
    def __init__(self, *banks):
        self.banks = []
        for i in banks:
            self.banks.append(i)

    def checkInterestInformation(self):
        return_str = ""
        for i in self.banks:
            return_str += f"{i.getInterestRate()}\n"

        return return_str


BankA = Bank("BankA", 0.04)
BankB = Bank("BankB", 0.0395)
BankC = Bank("BankC", 0.035)

app = InterestApp(BankA, BankB, BankC)

print(app.checkInterestInformation())
