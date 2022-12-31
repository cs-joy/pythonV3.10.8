# A tuple consists of a number of values separated by commas, for instance:

t = 23145, 76432, 4256, 'hello', 765, 'world', 'hello world', 8765, 'through t'
print(t)
print(t[8])

# Tuples may be nested:
nested = t, (123, 654, 321)
print(nested)

# Tuples are immutable
#nested[3] = 56789 # 'tuple' object does not support item assignment


# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)

'''

As you see, on output tuples are always enclosed in parentheses, so that nested tuples are interpreted correctly; they may be input with or without surrounding parentheses, although often parentheses are necessary anyway (if the tuple is part of a larger expression). It is not possible to assign to the individual items of a tuple, however it is possible to create tuples which contain mutable objects, such as lists.

Though tuples may seem similar to lists, they are often used in different situations and for different purposes. Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking (see later in this section) or indexing (or even by attribute in the case of namedtuples). Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.

A special problem is the construction of tuples containing 0 or 1 items: the syntax has some extra quirks to accommodate these. Empty tuples are constructed by an empty pair of parentheses; a tuple with one item is constructed by following a value with a comma (it is not sufficient to enclose a single value in parentheses). Ugly, but effective. For example:

'''

empty = ()
