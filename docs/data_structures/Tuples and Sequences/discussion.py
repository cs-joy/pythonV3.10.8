# A tuple consists of a number of values separated by commas, for instance:

t = 23145, 76432, 4256, 'hello', 765, 'world', 'hello world', 8765, 'through t'
print(t)
print(t[8])

# Tuples may be nested:
nested = t, (123, 654, 321)
print(nested)

# Tuples are immutable
nested[3] = 56789 # 'tuple' object does not support item assignment