
# mode for a files in python
# 1. `r` for only want read the file informations
# 2. `w` for just writing a file means write new informations, existing new informations 
# 3. `a` stands for append, if you use this mode then you can append a such of new informations into the file but can't able to 
#        modify or change any informations of the file 
# 4. `r+` means reading and writing, all the power of reading and writing a file

employee_file = open("E:/GitHub/pythonV3.10.8/reading_files/employees.txt", "r")
# employee_file = open("E:/GitHub/pythonV3.10.8/reading_files/employees.txt", "w")

# check if the file is read able
# readable() - it's can tell us whether are not we can read the file and this function # return boolean value
"""
print(employee_file.readable()) # give us True value but when file mode is not reading("r") like writing("w") then this function give us False value
"""

# whether we can figure out the file is read able(means True) using readable function
# after than we use read() to read the file
# :::note::: if file is not read able that means we can't use read() to read the file, so before calling or using 
# read() make sure to use readable() to check out ,, is it True or False
# let's actually read it. so
"""
print(employee_file.read(), "\n") # read() - spread out all the informations of the file
"""

# as well as we can read an individual line of this file
# readline() - read individual line of the file
'''
print(employee_file.readline()) # read first line and change cursor to the next line of the file
print(employee_file.readline()) # prints second line of the file
print(employee_file.readline()) # prints third line of the file and so on...
'''

# there have another way that is better doing that
# readlines() - it's basically takes all of the lines inside of our file and put them inside of a list
'''
print(employee_file.readlines())
'''

# access the specific line of the file
'''
print(employee_file.readlines()[1]) # [index]
'''

# as well as you can use readlines() with a for loop
for employee in employee_file.readlines():
    print(employee)



# as well as should be need to close the file otherwise no longer able to access the file
employee_file.close() # make sure to close the file


# thus the basics of reading a file in read mode