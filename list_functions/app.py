
lucky_numbers = [42, 4, 8, 15, 16, 23]
friends = ["Kevin", "Toby", "Karen", "Jim", "Oscar", "Toby"]

# extend() - extend function will basically allow to take a list and append another list
friends.extend(lucky_numbers)

print(friends)

# append() - as well as we can also just add individually elements onto a list using append()
# in append function it always gonna add them item on the end of the list
friends.append("Creed")
print(friends)

# insert() - for inserting a element in a specific index
friends.insert(1, "Kelly") # all of this other values gonna be get push to the right one index position
print(friends)


# remove() - for removing a value from a list
friends.remove("Jim")
print(friends)

"""
# clear() - we can completely remove the list or say reset the list using this function
friends.clear()
print(friends)
"""

# pop() - basically pop() can likely to do pop an item of the list 
# that's mean it should always remove the last element of the list
friends.pop()
print(friends)

# index() - this is gonna tell me the index of the searching element
print(friends.index("Oscar"))
# print(friends.index("Joy")) # should give us error

# we can also count the number of similar element in the list using count()
print(friends.count("Toby"))

# friends = ['Kevin', 'Kelly', 'Toby', 'Karen', 'Oscar', 'Toby', 4, 8, 15, 16, 23, 43] # should give us-[TypeError: '<' not supported between instances of 'int' and 'str'
friends = ["Kevin", "Toby", "Karen", "Jim", "Oscar", "Toby"]
# we can also sort the list in ascending order using sort()
friends.sort()
print(friends)
# we can also sort in lucky_numbers variable
lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers = [42, 4, 8, 15, 16, 23]
# reverse() - reverse a list
lucky_numbers.reverse()
print(lucky_numbers)

# copy() - copying all the elements of the list
friends2 = friends.copy() # friends2 is gonna have all the same attributes as friends
print(friends2)