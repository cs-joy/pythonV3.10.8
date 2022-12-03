# inheritance - where we can define a bunch of attributes and functions inside of the class 
# then we can create another class and we can inherit all those attributes


from Chefs import Chef
from ChineseChefs import ChineseChef
from ChineseChefs import InheritanceChineseChef

myChef = Chef()
myChef.make_special_dish()

# not inherit
myChineseChef = ChineseChef()
myChineseChef.make_special_dish()

# inherit
inheritChef = InheritanceChineseChef()
inheritChef.make_chicken()
inheritChef.make_special_dish()
