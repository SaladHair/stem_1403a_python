"""
class method

@classmethod
"""


class Tool:
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1
        # cls.count += 1

    @classmethod
    def getToolCount(cls):
        # access class attribute with cls
        return cls.count

    @classmethod
    def printToolCount(cls):
        # access class attribute with cls
        print(cls.count)


# test
Tool.getToolCount()

tool1 = Tool("Hammer")
print(Tool.getToolCount())

Tool.printToolCount()
