"""
single
"""


class A:
    pass


class B(A):
    pass


print(B.__mro__)