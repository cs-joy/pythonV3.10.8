# "a" - Append - will append to the end of the file

f = open('E:/GitHub/pythonV3.10.8/file_handling/write/append_data.txt', 'a')

f.write('hello everyone! how is going?')
f.close()


#open and read the file after the appending:
file = open('E:/GitHub/pythonV3.10.8/file_handling/write/append_data.txt', 'r')

print(file.read())
file.close()
