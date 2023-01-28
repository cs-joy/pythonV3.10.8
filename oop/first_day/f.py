class Item:
    # magic method - __init__()
    def __init__(self):
        pass

    def calculate_area(self, x, y):
        return x * y

item1 = Item()

# two attributes
# 1. height 2. width
item1.height = 7.34
item1.width = 9.15

print(item1.calculate_area(item1.height, item1.width))