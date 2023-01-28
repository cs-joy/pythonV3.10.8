class Item:
    # magic method - __init__()
    def __init__(self, name):
        print(f"An instance created: {name}")
        self.name = name # dynamic attribute assignment

    def calculate_total_price(self, x, y):
        return x * y

item1 = Item("Phone")
# two attributes
# 1. price 2. quantity
item1.price = 700
item1.quantity = 9



item2 = Item("Laptop")
item2.price = 700
item2.quantity = 9

print(item1.name)
print(item2.name)