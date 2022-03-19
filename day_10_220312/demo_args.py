"""
*args
"""

print()
print("====================")

print(1)
print("====================")

print(1, 2)
print("====================")

print(1, 2, 3)
print("====================")

print(1, 2, 3, 4, 5, 6, 7, 8, 9)
print("====================")


def foo(*args):
    for i in args:
        print(i)


foo('a', 'b', 'c')

# =======================================


def testMe(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
testMe(**kwargs)

# =======================================

"""
Challenge:
How to transform kwargs format to args format?
"""


def testMe2(**kwargs):
    for i in kwargs:
        print(f"{i}:", kwargs[i])


kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
testMe2(**kwargs)

# =======================================


def foo2(**kwargs):
    print(type(kwargs))

    for i in kwargs:
        print(i, kwargs[i])


foo2(arg3=3, arg2=2, arg1=1)
