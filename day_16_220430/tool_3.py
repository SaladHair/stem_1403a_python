"""
adding properties by assignment
"""


class Tool:
    count = 0

    def __init__(self, name):
        self.name = name
        # self.count = 99
        Tool.count += 1
        # self.count = 99


# test
tool1 = Tool("hammer")
print(f'{tool1.count} tool(s) is(are) created.')
print()

# adding a property into the object tool1
tool1.count = 99
print(f'The instance tool1 has extra property: count')
print(f'{tool1.count} tools are created.')
print()

tool2 = Tool("Big hammer")
print(f'{tool2.count} tool(s) is(are) created.')
print()

'''
print(f'Now instance property has nothing to do with class property: count')
print(f'{Tool.count} tools are created.')

tool2 = Tool("drill")
print(f'{Tool.count} tool(s) is(are) created.')
print()

tool3 = Tool("screwdriver")
print(f'{tool3.__class__.count} tools are created.')
'''