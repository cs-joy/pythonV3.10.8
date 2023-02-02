# v1.0
'''
def distance(x1, y1, x2, y2):
    return 0.0

print(distance(1, 2, 4, 6))
'''

# v1.1
'''
def distance(x1, y1, x2, y2):
    dx = x2- x1
    dy = y2 - y1
    print('dx is: ', dx)
    print('dy is: ', dy)
    return 0.0

print(distance(1, 2, 4, 6))
'''

# v1.2
'''
def distance(x1, y1, x2, y2):
    dx = x2- x1
    dy = y2 - y1
    dsquared = dx ** 2 + dy ** 2
    print('dsquared= ', dsquared)
    return 0.0

print(distance(1, 2, 4, 6))
'''


# v1.3
import math as mth
def distance(x1, y1, x2, y2):
    dx = x2- x1
    dy = y2 - y1
    dsquared = dx ** 2 + dy ** 2
    result = mth.sqrt(dsquared)
    return result
### final product


print(distance(1, 2, 4, 6))
