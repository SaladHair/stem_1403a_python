"""
[Homework]
Date: 2022-03-05
Due date: 2022-03-11
1. Rewrite codes for initialization in all cases of inheritance.
Hints:
One case per python file
Do not submit them to SLACK.
Keep them on your computer.
2. Write a summary of all cases of initialization
Example,
case 1. title and description
case 2. title and description
case 3. title and description
"""

"""
Single inheritance

Case 1. super_init_1: child directly inherits init() of parent

child class does not initialize itself, directly inherits parent's init()
no properties

Case 2. super_init_1b: child directly inherits init() of parent

again, child class directly inherits parent's init()
1 property in parent
number of properties must match

Case 3. super_init_2: child overrides init() of parent and use its own init()

child has init() but doesnt call parent init()
no properties

Case 4. super_init_2b: child overrides init() of parent and use its own init()

child has init() but doesnt call parent init()
child has a property but parent does not 

Case 5. super_init_2c: child overrides init() of parent and use its own init()

child has init() but doesnt call parent init()
both child and parent have a property
parameters must match with child but not with parent
parent properties cannot be accessed since parent is not initialized

Case 6. super_init_2d: child overrides init() of parent and use its own init()

child has init() and calls parent init()
both child and parent have a property
parameters must match with both parent and child
child inits with both parent properties and own properties

Case 7. super_init_2e: child overrides init() of parent and use its own init()

child has init() and calls parent init()
both child and parent have a property
parameters must match with both parent and child
child inits with both parent properties and own properties
parameters are reversed
init() successful but can lead to confusion

"""

"""
Multilevel inheritance

Case 1. multilevel_init_1: grandson directly inherits init() of grandparent

grandson class does not initialize itself, son doesn't have an init(), grandson directly inherits grandparent's init()
no properties

Case 2. multilevel_init_2: grandson directly inherits init() of son

grandson class does not initialize itself, grandson directly inherits son's init()
grandparent has init() but is not accessed due to mro, after the son init() is found the search stops.
no properties

Case 3. multilevel_init_3: grandson overrides init() of son and grandparent and use its own init()

grandson class has init but does not call init of son and grandparent
no properties

Case 4. multilevel_init_4: grandson overrides init() of son and grandparent and use its own init()

grandson class has init and calls init of son, but son does not have init so son inherits grandparent's init()
grandparent has a property
parameters must match properties

Case 5. multilevel_init_4b: grandson overrides init() of son and grandparent and use its own init()

grandson class has init and calls init of son
grandparent has a property
grandparent init is not called due to mro
son and grandson do not have properties
parameters must match properties, in this case there are no properties

Case 6. multilevel_init_4c: grandson overrides init() of son and grandparent and use its own init()

grandson class has init and calls init of son
grandparent has a property
grandparent init is not called due to mro
son has a property
grandson does not have properties
parameters must match properties, 1 property for son

Case 7. multilevel_init_5: grandson overrides init() of son and grandparent and use its own init()

grandson class has init and calls init of son and son calls init of grandparent
grandparent has a property
son has a property
grandson does not have properties
parameters must match properties, 1 property for son and 1 for grandparent

Case 8. multilevel_init_5b: grandson overrides init() of son and grandparent and use its own init()

grandson class has init and calls init of son and son calls init of grandparent
grandparent has a property
son has a property
grandson has a property
parameters must match properties, 1 property for son, 1 for grandparent and 1 for grandson
"""

"""
Multiple inheritance

Case 1. multiple_init_1: : child directly inherits init() of parent

child class does not initialize itself, directly inherits according to mro
parenta and parentb have inits, but parentb init is not accessed because child inheritance is ParentA before ParentB

if the order of child inheritance is switched such as Child(ParentB, ParentA), parentb's init will be called.

Case 2. multiple_init_2: : child overrides init() of parent and use its own init()

child has init() but doesnt call parents init()
both parents are not accessed
no properties

Case 3. multiple_init_3: : child overrides init() of parent and use its own init()

child has init() but doesnt call parents init()
both parents are not accessed
parenta has a property but the property is not visible
child has a property and the property is required in parameters

Case 4. multiple_init_3b: : child overrides init() of parent and use its own init()

child has init() but doesnt call parents init()
both parents are not accessed
parenta has a property but the property is not visible
child has 2 property and the properties are required in parameters
child property has the same name as parent property but parent is not accessed

Case 5. multiple_init_3c: : child overrides init() of parent and use its own init()

child has init() and calls parent init
parenta is accessed but not parentb due to mro
parenta has a property 
child has a property
parameters have to match the properties

Case 6. multiple_init_3d: : child overrides init() of parent and use its own init()

child has init() and calls parent init
parenta is accessed but not parentb due to mro
parenta does not have a property
parentb has a property but is not accessed
child has a property
parameters have to match the properties but parentb properties aren't accessed, so only child and parenta properties 
need to be matched, parentb properties are not visible
"""