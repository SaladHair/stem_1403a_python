"""

"""


class GrandParent:
    # not used
    def __init__(self):
        print('GrandParent __init__() called')


class Son(GrandParent):
    # not used
    def __init__(self):
        print('Son __init__() called')


class GrandSon(Son):
    def __init__(self):
        print('GrandSon __init__() called')


# main
gs1 = GrandSon()
