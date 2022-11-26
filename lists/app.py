# basics of working with list

# in python when you dealing with large amount of data
# then you want to make sure that manage it and organize it properly

# A list is just a structure that we can use inside of python to stored a list of the informations
# so, we can take a bunch of different data values we can put them inside a list and its allows us to 
# organize them and keep track them a lot easier

#friends = ["Kevin", 2, "Jim", False]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends)

# print a specific element inside of friends list
print(friends[1])

# other way to print the specific value
print(friends[-1])

# another way to print out specific values
print(friends[1:]) # print from index 1 of friends variable

# another way to print out a range of element
print(friends[2:4]) # print index 1 and index 2 element. this means before the index of 3

# modifying
friends[1] = "Mike"
print(friends[1])

#-----------------------------------