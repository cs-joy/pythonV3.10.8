# "w" - Write - will overwrite any existing content

f = open('E:/GitHub/pythonV3.10.8/file_handling/write/write_data.txt', 'w')

f.write('"Woops! I have deleted the old content and overwrite the this content!"')
f.close()


file = open('E:/GitHub/pythonV3.10.8/file_handling/write/write_data.txt', 'r')
print(file.read())
file.close()


'''
Note::::: the "w" method will overwrite the entire file.
'''
