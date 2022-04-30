"""
add property
"""


class Tool:
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1


# test
tool1 = Tool("screwdriver")
print(f'{tool1.count} tools are created')
print()

tool1.count = 99
print(f'The instance tool has extra property: count')
print(f'{tool1.count} tools are created')
print()

print('Now instance property has nothing to do with class property: count')
print(f'{Tool.count} tools are created')
print()

tool2 = Tool("saw")
print(f'{Tool.count} tools are created')

tool3 = Tool("hammer")
print(f'{tool3.__class__.count} tools are created')
