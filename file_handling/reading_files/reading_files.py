file = open("E:/GitHub/pythonV3.10.8/file_handling/reading_files/read_file.txt", "r")

#print(file.read())

# Read Only Parts of the File
#print(file.read(3)) # Return the 5 first characters of the file:

# Read lines
# print(file.readline())

# By calling readline() two times, you can read the two first lines:
#print(file.readline())
#print(file.readline())


# By looping through the lines of the file, you can read the whole file, line by line:
''''
for text_line in  file:
    print(text_line)
'''

# close file
# It is a good practice to always close the file when you are done with it.
print(file.readline())
file.close()
'''
Note::: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.
'''