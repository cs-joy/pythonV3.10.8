import math as mth
def distance(x1, y1, x2, y2):
    return mth.sqrt((x2- x1) ** 2 + (y2 - y1) ** 2)

print(distance(1, 2, 4, 6))