"""
I wake up
If i'm hungry
    I eat breakfast

I leave my house
If it's cloudy
    I bring an umbrella
Otherwise
    I bring sunglass

I'm at a restaurent
If i want meat
    I order a steak
Otherwise If i want pasta
    I order spaghetti & metaballs
Otherwise
    I order salad
"""



# if
is_male = True
if is_male:
    print("You are a male")


# else
is_num = False
if is_num:
    print("This a number")
else:
    print("This is not a numer")

# combination
is_string = False
is_char = False
# with or operator
if is_string or is_char:
    print("this is a string or character or both")
else:
    print("this is neither string nor character")

is_string = True
is_char = True
# with and operator
# `and` except both of this condition true
if is_string and is_char:
    print("this is a combination of string and character")
else:
    print("this is either not string or not character or both")


# so, thus the basics of `and` `or`

is_male = False
is_tall = False
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not male but tall")
else:
    print("You are not a male and not tall")