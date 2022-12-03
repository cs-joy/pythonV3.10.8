
# appending - add information
'''
student_file = open("E:/GitHub/pythonV3.10.8/writing_to_files/students.txt", "a")
isWriteable = student_file.writable()
if isWriteable:
    student_file.write("\nKammy - CSE") # `\n` escape character
'''

'''
# writing - write information
student_file = open("E:/GitHub/pythonV3.10.8/writing_to_files/students.txt", "w")
isWriteable = student_file.writable()
if isWriteable:
    student_file.write("Jahangir - CSE")
'''

'''
# writing - create new file and write information
student_file = open("E:/GitHub/pythonV3.10.8/writing_to_files/cse_students.txt", "w")
isWriteable = student_file.writable()
if isWriteable:
    student_file.write("Nayem - CSE")
'''

# writing - create new file and write information
# create web page
student_file = open("E:/GitHub/pythonV3.10.8/writing_to_files/index.html", "w")
isWriteable = student_file.writable()
if isWriteable:
    student_file.write("<h1>Hello World!</h1>")

student_file.close()