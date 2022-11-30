# for loop - a for loop is a special type of loop in python which allows us to loop over
# different collections of items

# with string
for letter in "Sharp Academy": # this is gonna say, `for every letter inside of Sharp Academy i want to do something`
    print(letter)

# with arrays/list
friends = ['Kelvin', 'Klein', 'Jim', 'Karen']
for friend in friends:
    print(friend)


# with series of numbers
for number in range(10):
    print(number) # print 0-9

print('\n')

# range of  numbers
for num in range(2, 8):
    print(num) # print 2-7

print('\n')

# find out length of the array/list
employee = ['Kiran', 'Qualam', 'Jenny', 'Strophy']

for index in range(len(employee)):
    print(employee[index])