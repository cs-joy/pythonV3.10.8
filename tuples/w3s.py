# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# declaring / create tuple
student = ("John", "Tom", "Jim", "Jerry", "Tom")
print(student)

# create only one tuple element
cat_name = ("era",)
print(cat_name)


# use the tuple() constructor to make a tuple.
employeer = tuple(("Jenny", "Kelvin", "Koerain", "Mike", "Joy", "Shangu"))
print(employeer)



# access tuples
# access tuple items by referring to the index number, inside square brackets
print(student[2]) # Jim

# negative indexing
print(student[-2]) # Tom

# range of index
print(student[-2:]) # ('Jerry', 'Tom')
print(student[1:]) # ('Tom', 'Jim', 'Jerry', 'Tom)

print(student[1:4]) # ('Tom', 'Jim', 'Jerry')

print(student[:-2]) # ('John', 'Tom', 'Jim')


# range of negative index
print(student[-4:-2]) # ('Tom', 'Jim')

# To determine if a specified item is present in a tuple use the in keyword
if "Joy" in employeer:
    print("Yes, `Joy` is in the employeer tuple") # return the index
else:
    print("No found!")