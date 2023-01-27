'''
If an exception occurs when we are performing some operation with the file, the code exits without closing the file.
 A safer way is to use a try...finally block.
'''

f = open('E:/GitHub/pythonV3.10.8/file_handling/programiz/exception_handling_file.txt', 'r')
try:
    print(f.read())

finally:
    f.close()

'''
Here, we have closed the file in the finally block as finally always executes, 
and the file will be closed even if an exception occurs.
'''