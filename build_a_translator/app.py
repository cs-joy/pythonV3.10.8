"""
# v1
def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou": # not efficient
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translator(input("Enter a phrase: ")))
"""


"""
# v2
def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou": # efficient
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translator(input("Enter a phrase: ")))
"""


# v3
def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou": # efficient
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translator(input("Enter a phrase: ")))