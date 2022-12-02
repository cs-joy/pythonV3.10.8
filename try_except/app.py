# caching errors in python
"""
number  = int(input("Enter a number: "))
print(number)
"""

# try..except block - a try...except block is basically allow your program to try out a piece of code and 
# if everything goes well then great 
"""
number  = int(input("Enter a number: "))
print(number)
"""
# like we can try out entering the number but if thery don't entering correct number / like enter a string
# then we can basically handle the error what is broke our program

# so,,
"""
try:
    number  = int(input("Enter a number: "))
    print(number)
except:
    print("Ivalid input")
"""

# we use try..except block basically for protect our program


# value = 10/0 # here we can't do that, it's not possible, python give us error
"""
try:
    value = 10/0
    number  = int(input("Enter a number: "))
    print(number)
except:
    print("Ivalid input")
"""


"""
# except 2 more errors
try:
    # value = 10/0
    number  = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("Invalid input")
"""


# print out actual error notation
try:
    #answer = 10/0
    number  = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err) # print our specific error got through
except ValueError as err:
    print(err)

# a base practise in python is to use the specific error like 
# `except ZeroDivisionError:` or, `except ZeroDivisionError as err:` 
# we don't want to do is just say `except:`