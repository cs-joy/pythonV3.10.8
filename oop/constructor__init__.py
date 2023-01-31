class Product:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):

        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        self.name = name
        self.price = price
        self.quantity = quantity

        Product.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Product('{self.name}', '{self.price}', '{self.quantity}')"


item1 = Product("Ball", 25, 5)
item2 = Product("Phone", 300, 80)
item3 = Product("Laptop", 1000, 9)
item4 = Product("Speaker", 115, 10)
item5 = Product("Cable", 55, 100)


print(Product.all) # print out object
'''
for instance in Product.all:
    print(instance.name) # print name of product
'''