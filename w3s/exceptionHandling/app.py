"""
- the `try` block lets you test a block of code for errors
- the `except` block lets you handle the error
- the `else` block lets you execute code when there is no error
- the `finally` block lets you execute code, regardless of the result of the `try` and `except` blocks
"""

# example
# the try block will generate an exception, because x is not defined:
try:
    print(x)
except:
    print('An exception occurred!\n')


# Many Exceptions
# we can define as many exception blocks as you want, 
# e.g. if you want to execute a special block of code for a special kind of error:
x = 3
try:
    print("striker" + 3)
except NameError:
    print("Variable x is not defined\n")
except:
    print("Something else went wrong!\n")


# else
# the else keyword to define a block of code to be executed if no errors were raised:
try:
    print("Hello Walker")
except:
    print("Something went wrong!\n")
else:
    print("Nothing went wrong!\n")


# finally
# the `finally` block, if specified, will be executed regardless if the try block raises an error or not
try:
    print(a)
except:
    print("Something went wrong!")
finally:
    print("The `try except` is finished")
# This can be useful to close objects and clean up resources:

# another example
try:
    f = open("demo.txt")
    try:
        f.write("Lorem Ipsum")
    except:
        print("Something went wrong when writing to the file!")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file!")


# raise an exception
# we can choose to throw an exception if a condition occurs.
# To throw (or raise) an exception, use the raise keyword.

# example
# raise and error and stop the program is z is lower than 0
"""
z = -1
if z < 0:
    raise Exception("Sorry, no numbers below zero")
"""

# the `raise` keyword use to raise an exception
# we can define what kind of error to raise, and the text to print to the user.
a = "walker"
if not type(a) is int:
    raise Exception("Sorry, Only integers are allowed!")


# this are basics of exception handling