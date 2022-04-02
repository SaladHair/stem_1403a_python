"""
[Homework]
Date: 2022-03-26
Due date: 2022-04-01
2. Rewrite Bank Interest
"""


class Bank:
    def __init__(self, name, interest_rate):
        self.name = name
        self.interest_rate = interest_rate

    def getInterestRate(self):
        return f"Bank's interest rate is {str(self.interest_rate)} ({str(round(self.interest_rate*100, 2))}%)"


class BankA(Bank):
    def getInterestRate(self):
        return f"BankA's interest rate is {str(self.interest_rate)} ({str(round(self.interest_rate*100, 2))}%)"


class BankB(Bank):
    def getInterestRate(self):
        return f"BankB's interest rate is {str(self.interest_rate)} ({str(round(self.interest_rate*100, 2))}%)"


class BankC(Bank):
    def getInterestRate(self):
        return f"BankC's interest rate is {str(self.interest_rate)} ({str(round(self.interest_rate*100, 2))}%)"


class InterestApp:
    def __init__(self, *banks):
        self.banks = []
        for i in banks:
            self.banks.append(i)

    def checkInterestInformation(self):
        return_str = ""
        for bank in self.banks:
            interest_rate = bank.getInterestRate()
            return_str += f"{interest_rate}\n"

        return return_str


BankA = BankA("BankA", 0.04)
BankB = BankB("BankB", 0.0395)
BankC = BankC("BankC", 0.035)

app = InterestApp(BankA, BankB, BankC)

print(app.checkInterestInformation())
