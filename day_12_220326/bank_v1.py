"""

"""


class Bank:
    def __init__(self, interest_rate=None):
        self.interest_rate = interest_rate

    def getInterestRate(self):
        return self.interest_rate


class BankA(Bank):
    def getInterestRate(self):
        return self.interest_rate


class BankB(Bank):
    def getInterestRate(self):
        return self.interest_rate


class BankC(Bank):
    def getInterestRate(self):
        return self.interest_rate


class InterestInfoApp:
    def queryInterestRate(self, bankObj):
        result = bankObj.getInterestRate()
        return result


bank1 = BankA(0.04)
bank2 = BankB(0.0395)
bank3 = BankC(0.035)

myapp = InterestInfoApp()

print("Query interest rate of bank A")
print(f"{myapp.queryInterestRate(bank1):.3%}")
print()

print("Query interest rate of bank B")
print(f"{myapp.queryInterestRate(bank2):.3%}")
print()

print("Query interest rate of bank C")
print(f"{myapp.queryInterestRate(bank3):.3%}")
print()
