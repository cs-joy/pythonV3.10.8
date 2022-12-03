class Employee:
    def __init__(self, name, position, TER, salary):
        self.name = name
        self.position = position
        self.TER = TER
        self.salary = salary

    def on_honor_roll(self):
        if self.TER >= 5:
            return True
        else:
            return False