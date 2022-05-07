"""
static method
"""


class Foo:

    @staticmethod
    def mymethod():
        print("the static method: mymethod()")


# test
# access via class name
Foo.mymethod()

# access via instance
foo1 = Foo()
foo1.mymethod()

foo2 = Foo()
foo2.mymethod()
