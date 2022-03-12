"""

"""


class GrandParent:
    def __init__(self, name):
        print('GrandParent __init__() called')
        self.name = name


class Son(GrandParent):
    pass


class GrandSon(Son):
    def __init__(self, name):
        print('GrandSon __init__() called')
        super().__init__(name)


# main
gs1 = GrandSon("Peter")
print(gs1.name)
