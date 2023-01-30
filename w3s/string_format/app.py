# format() method allows you to format selected parts of a string.

# Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?

# To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:

price  = 808.56
itemPrice = "The price is {} dollers"
print(itemPrice.format(price))


#  Format the price to be displayed as a number with two decimals:
weight = 46
txt = "weight is {:.2f} kg"
print(txt.format(weight))


# multiple values
story = "Hello {}, Welcome to the {} world. Here we willl discuss about the {}."
print(story.format("Mike", "Programming", "Science & Technology"))


txt1  = "Hello {programming_language}. How you feel to get a new {member}?"
print(txt1.format(programming_language="python", member="john"))


# ref:: https://www.w3schools.com/python/ref_string_format.asp