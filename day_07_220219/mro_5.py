"""
hybrid
"""


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D1(B, C):
    pass


class D2(C, B):
    pass


print(D1.__mro__)
print(D2.__mro__)
