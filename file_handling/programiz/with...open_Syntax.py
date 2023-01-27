# we can use the with...open syntax to automatically close the file. For example,

with open("E:/GitHub/pythonV3.10.8/file_handling/programiz/with..open_file.txt", "r") as file:
    read_content = file.read()
    print(read_content)

'''
Note: Since we don't have to worry about closing the file, make a habit of using the with...open syntax.
'''