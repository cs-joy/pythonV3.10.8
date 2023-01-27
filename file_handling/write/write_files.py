f = open('E:/GitHub/pythonV3.10.8/file_handling/write/write_data.txt', 'w')

f.write('say, hello to the negotitation world')
f.close()


file = open('E:/GitHub/pythonV3.10.8/file_handling/write/write_data.txt', 'r')
print(file.read())
file.close()
