import os

#file = "E:/GitHub/pythonV3.10.8/file_handling/delete_files/d_files.txt"

#os.remove(file)


# To avoid getting an error, you might want to check if the file exists before you try to delete it:

# for example, Check if file exists, then delete it:
'''
if os.path.exists("E:/GitHub/pythonV3.10.8/file_handling/delete_files/d_files.txt"):
    os.remove("E:/GitHub/pythonV3.10.8/file_handling/delete_files/d_files.txt")
else:
    print("File doesn't exists")
'''


# Delete folder
# To delete an entire folder, use the os.rmdir() method:
#os.rmdir("E:/GitHub/pythonV3.10.8/file_handling/delete_files/entire_folder")

if os.path.exists("E:/GitHub/pythonV3.10.8/file_handling/delete_files/entire_folder"):
    os.rmdir("E:/GitHub/pythonV3.10.8/file_handling/delete_files/entire_folder")
else:
    print("Folder doesn't exists")

# Note: You can only remove empty folders.