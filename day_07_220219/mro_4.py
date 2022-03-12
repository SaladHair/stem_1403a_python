"""
multiple
"""


class A:
    pass


class B:
    pass


class C1(A, B):
    pass


class C2(B, A):
    pass


print(C1.__mro__)
print(C2.__mro__)