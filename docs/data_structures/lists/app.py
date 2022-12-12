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