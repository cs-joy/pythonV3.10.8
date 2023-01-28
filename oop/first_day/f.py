class Item:
    # magic method - __init__()
    def __init__(self, name: str, price: float, quantity=0):
        self.name = name # dynamic attribute assignment
        self.price = price
        self.quatity = quantity
    

    def calculate_total_price(self):
        return self.price * self.quatity



item1 = Item("Phone", 700, 9)


item2 = Item("Laptop", 30000, 5)


print(item1.calculate_total_price())

print(item2.calculate_total_price())


# ref: https://www.youtube.com/watch?v=Ej_02ICOIgs