# tuple - tuple is a type of data structure which basically means container where we can store different values
# tuple is a immutable this means tuple can be changed or be modified once it is created then you can't 
# modify or can't change it as i mean you can't change any of the element inside of a tuple
# so, once tuple is created it's as it is, you can't changed

coordinates = (4, 5)
# coordinates[1] = 10  # it should give us an [TypeError: 'tuple' object does not support item assignment
print(coordinates)
print(coordinates[1])

coordinates = [(4, 5), (2, 7), (6, 1), (9, 4)]
print(coordinates)
print(coordinates[2])