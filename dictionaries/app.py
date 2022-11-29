# dictionaries - a dictionaries is a special structure in python which allows us 
# to store informations called `key` `value` pairs

monthConversions = {
    "Jan": "January", # `key: value` note- all of the keys have to be unique
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

# access value- first way
print(monthConversions["Jun"])

# access value- second way
print(monthConversions.get("Aug"))

# if key is not right then python give us ``KeyError``
# like...
try:
    print(monthConversions["Luv"])
except:
    print("key is not found in your dictionary!")

# if key is not present in the dictionaries then this function should say ``None``
print(monthConversions.get("Hel"))

# another way with get()
print(monthConversions.get("Lov", "Not a valid Key"))

country_list = {
    0: "Bangladesh",
    1: "United States",
    2: "United Kingdom",
    3: "India",
    4: "Pakisthan",
    5: 'Canada'
}

print(country_list[0])

print(country_list.get(4))

print(country_list.get(6, "Not a valid Key"))