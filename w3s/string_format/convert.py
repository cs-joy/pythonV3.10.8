import win32com.client 
import os
import re
rootdir ='D:\id'
app = win32com.client.Dispatch('Word.Application')
try:
    
    app.Visible = True
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            fullpath = os.path.join(*[subdir, file])
            if file.endswith(".docx"):
                out_name = file.replace("docx", r"txt")
                in_file = os.path.abspath(rootdir + "\\" + file)
                out_file = os.path.abspath(rootdir + "\\" + out_name)
                doc = app.Documents.Open(in_file)
                content = doc.Content.Text
                print('Exporting'), out_file
                doc.SaveAs(out_file, FileFormat=7)
                doc.Close()
except Exception as e:
    print(e)
finally:
    app.Quit()