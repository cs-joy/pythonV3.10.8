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

''''

which is more concise and readable.

A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. 
The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it. 
For example, this listcomp combines the elements of two lists if they are not equal:

'''
print(
    [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
)

# and it's equivalent to
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))

print(combs)


'''
Note how the order of the `for` and `if` statements is the same in both these snippets.

If the expression is a tuple (e.g. the (x, y) in the previous example), it must be parenthesized.
'''

vec = [-4, -2, 0, 2, 4]
# create new list with values doubled

# ref :: https://docs.python.org/3/tutorial/datastructures.html