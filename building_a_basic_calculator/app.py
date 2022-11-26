

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

result = num1 + num2

print(result)

# so we should be need to convert string to number
# convert a string to number in two ways-
# first one is- with int() - note:: int() can't hold decimal numbers
"""
result = int(num1) + int(num2)
print(result)
"""
# second one is- with float()
result = float(num1) + float(num2)
print(result)