"""
hierarchical
"""


class A:
    pass


class B(A):
    pass


class C(A):
    pass


print(B.__mro__)
print(C.__mro__)