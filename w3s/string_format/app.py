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

txt2 = "I want {} pieces of item number {} for {} dollars."
print(txt2.format(3, 57, 69))


# index number

quantity = 17
itemno = 290
price = 617
user_order = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(user_order.format(quantity, itemno, price))



# ref:: https://www.w3schools.com/python/ref_string_format.asp