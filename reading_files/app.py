
# mode for a files in python
# 1. `r` for only want read the file informations
# 2. `w` for just writing a file means write new informations, existing new informations 
# 3. `a` stands for append, if you use this mode then you can append a such of new informations into the file but can't able to 
#        modify or change any informations of the file 
# 4. `r+` means reading and writing, all the power of reading and writing a file

employee_file = open("employees.txt", "r")

# as well as should be need to close the file otherwise no longer able to access the file
employee_file.close() # make sure to close the file