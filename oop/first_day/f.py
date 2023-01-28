class Item:
    # magic method - __init__()
    def __init__(self, name):
        print(f"An instance created: {name}")

    def calculate_total_price(self, x, y):
        return x * y

item1 = Item("Phone")
# two attributes
# 1. price 2. quantity
item1.price = 700
item1.quantity = 9



item1 = Item("Laptop")
item1.price = 700
item1.quantity = 9