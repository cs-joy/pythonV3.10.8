from math import * # basically this gonna to do is go out and grab math functions

print(2)

print(-2)

print(2.345)

print(23456.4567)

# arithmatic operations
print(2 + 4)
print(2 + 4.06)

print(2 / 4)

print(4.15 * 2.0)

print(4 - 10.4)
print(5 - 7)

# specific order operation or say complex operation
print(2 * 5 + 2) # first 2 * 5 then 10 + 2 = 12

print(2 * (5 + 2)) # first 5 + 2 then 2 * 7 = 14

# modulus operator
print(11 % 3)

# with varibale
my_num = 5
print(my_num % 2)

# convert the number into a string
print(str(my_num) + ' is my favorite number.')

# when i wasn't convert the number to a string then python give us error and say...
# print(my_num + " is my favorite number.")

num = -2
# abs() - give us absolute value
print(abs(num)) # expected 2


# power
# pow() - 2 parameter required
# so, first parameter hold number and seocnd parameter hold the power that i want to take the number to
print(pow(5, 2)) # 5^2 (five square)

# max() - find out max number
print(max(3, 7))

# min() - find out min number
print(min(3, 7))

# round() - this is gonna allow us to round a number
print(round(9.4))
print(round(9.5))


# using the math modules or "from math import *"

# floor() - basically it just grab the lowest number
# it is essentially chop up the decimal point
print(floor(3.9))

# ceil() - opposite of floor()
print(ceil(3.9))

# square root
# sqrt() - essentially this return the square root of the number
print(sqrt(144))

# there have a lot of functions inside of the math modules, so go on google and search, how do they work?
# !bye