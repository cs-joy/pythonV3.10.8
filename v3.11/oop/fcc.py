class Item:
    def __init__(self, name: str, price: float, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("Phone", 328, 4)
print(item1.calculate_total_price())

item2 = Item("Laptop", 2000, 6)
print(item2.calculate_total_price())
