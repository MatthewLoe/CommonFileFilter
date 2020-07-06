import shutil
import os

def checkFile(target, directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename == target:
                return True

def compare(dir1, dir2):
    commonFiles = []
    
    for dirpath, dirnames, filenames in os.walk(dir1):
        for filename in filenames:
            check = checkFile(filename, dir2)
            if (check):
                commonFiles.append(filename)

    return commonFiles

def findFile(target, directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename == target:
                return os.path.join(dirpath, filename)

def removeFile(target, directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename == target:
                os.remove(os.path.join(dirpath,filename))

#Copies contents of source to destination directory                
def copyFiles(srcDir, targetDir):
    for dirpath, dirnames, filenames in os.walk(srcDir):
        for filename in filenames:
            if filename.endswith(".epub"):
                path = findFile(filename, srcDir)
                shutil.copy(path, targetDir+'\\'+filename)

dir1 = 'Books'
dir2 = 'ebooks'
common = 'CommonFiles'

"""
Code from here to block commentted code finds common files 
and copies them to separate folder, deleting from the 
compared directories.
"""
commonFiles = compare(dir1, dir2)

for ii in commonFiles:
    path = findFile(ii, dir1)
    shutil.copy(path, 'CommonFiles\\'+ii)
    removeFile(ii, dir1)
    removeFile(ii, dir2)

"""
Code below copies files from directory 1 and directory 2 to 
a specified destination.

dest = 'Epubs'

os.mkdir(dest)

copyFiles(dir1, dest)
copyFiles(dir2, dest)
"""