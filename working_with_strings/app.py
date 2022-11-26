# print string
print("Sharp Academy")

# insert new line
print("Sharp\nAcademy")

# \" to print out quotation mark(")
# \ scape character
print("Sharp\"Academy")

# with variable
phrase = "Sharp Academy"
print(phrase)

# concatenation - an concatenation is basically the process of taking a string and appending an another string
print(phrase + " is cool")

# function - a function is basically just little block of code that we can run and perform a specific operation for us
# convert to lower case
print(phrase.lower())
# convert to upper case
print(phrase.upper())

# check if the string is entirely upper case or lower case
# for check upper case
print(phrase.isupper())
# for check lower case
print(phrase.islower())

# we can convert it into upper case then check if it is upper
print(phrase.upper().isupper())


# find out length of the string
# figure out how many character inside this(phrase) string
print(len(phrase))

# [] square bracket
# get individual character inside of the string
print(phrase[0])

# index() - tell us where a specific character or string is located inside of a string
print(phrase.index("a"))

# replace() - replacing value inside of a string
print(phrase.replace("Sharp", "Tom"))

# check out other's function and see how do they work //using search on google