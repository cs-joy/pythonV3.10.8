# a class function is essentially a function that we can use inside of a class and can either 
# modify the object of that class give us specific information about those objects

from Employees import Employee

employee1 = Employee("Oscar", "Developer", 4.3, 75000)
employee2 = Employee("Jim", "UI/UX Designer", 5.4, 86000)

print(employee2.on_honor_roll())