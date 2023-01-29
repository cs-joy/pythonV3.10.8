class Item:
    # class attributes
    pay_rate = 0.8

    def __init__(self, name: str, price: float, quantity=0):
        # Run validation to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate


item1 = Item("Phone", 100, 1)
print(item1.calculate_total_price())

item2 = Item("Laptop", 1000, 3)
print(item2.calculate_total_price())

# definition of constructor and instances and attributes

print("#################")
#####################

print(Item.pay_rate)  # access class attribute directly
print(item1.pay_rate)  # access class attribute via instance1
print(item2.pay_rate)  # access class attribute via instance2

print("#################")
#####################
print(Item.__dict__)  # All the attributes for Class level
print(item1.__dict__)  # All the attributes for Instance level

print("#################")
#########################

item1.apply_discount()
print(item1.price)

item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)

# demonstration of Class and Instance level attributes
