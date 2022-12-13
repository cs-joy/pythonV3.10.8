'''

List comprehensions provide a concise way to create lists. 
Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.

'''

# For example, assume we want to create a list of squares, like:

squares = []
for x in range(10):
    squares.append(x**2)
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
###  this creates (or overwrites) a variable named x that still exists after the loop completes. 
#    We can calculate the list of squares without any side effects using:
squareList = list(map(lambda x: x**2, range(10)))
print(squareList) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# or, equivalently:
square = [x**2 for x in range(10)]
print(square) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# ref :: https://docs.python.org/3/tutorial/datastructures.html