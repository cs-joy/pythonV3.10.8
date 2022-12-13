fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

'''
list.count(x)
     Return the number of times x appears in the list.
'''
print(fruits.count('apple'))


'''
list.index(x[, start[, end]])
     Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

     The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. 
     The returned index is computed relative to the beginning of the full sequence rather than the start argument.
'''

print(fruits.index('banana'))

print(fruits.index('banana', 4)) # Find next banana starting at position 4



'''
list.reverse()
     Reverse the elements of the list in place.
'''
fruits.reverse()
print(fruits)


'''
list.append(x)
     Add an item to the end of the list. Equivalent to a[len(a):] = [x].
'''
fruits.append('grape')
print(fruits)


'''
list.sort(*, key=None, reverse=False)
     Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).
'''
fruits.sort()
print(fruits)


'''
list.pop([i])
     Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. 
     You will see this notation frequently in the Python Library Reference.)
'''
print(fruits.pop(5))
print(fruits)


'''
list.copy()
     Return a shallow copy of the list. Equivalent to a[:].
'''
copy_fruits = fruits.copy()
print(copy_fruits)



'''
list.clear()
     Remove all items from the list. Equivalent to del a[:].
'''
print(copy_fruits.clear())


'''
list.remove(x)
    Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
'''
fruits.remove('grape')
print(fruits)



'''
list.extend(iterable)
     Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable. 
'''
owner = ['mark', 'doe', 'john', 'mike', 'kelvin']
fruits.extend(owner)
print(fruits)



'''
list.insert(i, x)
      Insert an item at a given position. 
      The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
'''
fruits.insert(10, 'jim') # after 'mike'
print(fruits)



#### ref:: https://docs.python.org/3/tutorial/datastructures.html