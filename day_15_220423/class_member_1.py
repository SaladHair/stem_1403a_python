"""
class member
"""


class Foo1:
    pass


class Foo2:
    def m(self):
        pass


def main():
    #
    f1 = Foo1()
    f2 = Foo2()

    # data type
    a = 1
    b = 2

    print(type(a))
    print(type(b))

    print(type(f1))
    print(type(f2))


#
if __name__ == '__main__':
    main()

