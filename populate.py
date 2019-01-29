import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'Code_review.settings')

import os

class File:
    root = ""
    fileName = ""
    extention = ""
    
    def __init__(self, root, fileName, extention):
        self.root = root
        self.fileName = fileName
        self.extention = extention

pathOfDirectory = "C:\\Users\\tyagi\\Desktop\\Algorithm\\"

fileObj = list()
i = 0

for roots, directories, files in os.walk(pathOfDirectory):
    x = [".java", ".py", ".html"]
    for file in files:
        fileComp = os.path.splitext(file)       #fileComp stores the components of file, ie, filename and extention
        
        if fileComp[1] in x:

            fileObj.append(File(roots, fileComp[0], fileComp[1]))       #creating new File object for every file
            i+=1
        
print(str(i) + " file objects made.")



import django
django.setup()

from searchFiles.models import PathTable, FileTable

def populate():
    for index in range(len(fileObj)):
        c = add_path(fileObj[index].root)
        add_file(c,fileObj[index].fileName, fileObj[index].extention )


def add_path(path_str):
    p = PathTable.objects.get_or_create(Path = path_str)[0]
    # we need to save the changes we made!!
    p.save()
    return p

def add_file(path, File="", Ext=""):
    c = FileTable.objects.get_or_create(RootPath=path,FileName = File, Extension = Ext )[0]
    print(c)
    c.save()
    return c
# Start execution here!
if __name__ == '__main__':
    print("Starting population script...")
    populate()