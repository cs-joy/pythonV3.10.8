# format() method allows you to format selected parts of a string.

# Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?

# To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:

price  = 808.56
itemPrice = "The price is {} dollers"
print(itemPrice.format(price))