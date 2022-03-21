import os
import shutil
import getpass
from typing import List

User = getpass.getuser()
path = ('C:/Users/' + User + '/Downloads/')
names = os.listdir(path)
folder_name: List[str] = ['Programs Installers', 'Books', 'Pics', 'Documents', 'AHK Scripts', 'RARs',
                          'Cheat tables', 'SC2 Banks and Replays']
# for x in range(0, 8):
for x in range(0, len(folder_name)):
    if not os.path.exists(path + folder_name[x]):
        os.makedirs(path + folder_name[x])

subPath = (path + 'Documents/')
subNames = os.listdir(subPath)
folderSubNames: List[str] = ['Excels', 'Word', 'PDFs', 'Logs', 'Text Files', 'Power Points']
for x in range(0, len(folderSubNames)):
    if not os.path.exists(subPath + folderSubNames[x]):
        os.makedirs(subPath + folderSubNames[x])

for file_name in names:
    files = file_name.lower()
    if ".exe" in files or ".msi" in files or ".jar" in files and not \
            os.path.exists(path + 'Programs Installers/' + files):
        shutil.move(path + files, path + 'Programs Installers/' + files)

    if ".epub" in files and not os.path.exists(path + 'Books/' + files):
        shutil.move(path + files, path + 'Books/' + files)

    if ".png" in files and not os.path.exists(path + 'Pics/' + files):
        shutil.move(path + files, path + 'Pics/' + files)

    if ".jpg" in files or ".JPG" in files and not os.path.exists(path + 'Pics/' + files):
        shutil.move(path + files, path + 'Pics/' + files)

    if ".ahk" in files and not os.path.exists(path + 'AHK Scripts/' + files):
        shutil.move(path + files, path + 'AHK Scripts/' + files)

    if ".rar" in files or ".zip" in files or ".7z" in files and not \
            os.path.exists(path + 'RARs/' + files):
        shutil.move(path + files, path + 'RARs/' + files)

    if ".ct" in files and not os.path.exists(path + 'Cheat tables/' + files):
        shutil.move(path + files, path + 'Cheat tables/' + files)

    if ".SC2Bank" in files and not os.path.exists(path + 'SC2 Banks and Replays/' + files):
        shutil.move(path + files, path + 'SC2 Banks and Replays/' + files)

    # Breaking sub paths and paths apart

    if ".xls" in files or ".csv" in files and not os.path.exists(subPath + 'Excels/' + files):
        shutil.move(path + files, subPath + 'Excels/' + files)

    if ".doc" in files and not os.path.exists(subPath + 'Word/' + files):
        shutil.move(path + files, subPath + 'Word/' + files)

    if ".pdf" in files and not os.path.exists(subPath + 'PDFs/' + files):
        shutil.move(path + files, subPath + 'PDFs/' + files)

    if ".log" in files and not os.path.exists(subPath + 'Logs/' + files):
        shutil.move(path + files, subPath + 'Logs/' + files)

    if ".ppt" in files and not os.path.exists(subPath + 'Power Points/' + files):
        shutil.move(path + files, subPath + 'Power Points/' + files)

    if ".txt" in files and not os.path.exists(subPath + 'Text Files/' + files):
        shutil.move(path + files, subPath + 'Text Files/' + files)


for root, dirs, files in os.walk(path, topdown=False):
    for name in dirs:
        if len(os.listdir(os.path.join(root, name))) == 0:  # check whether the directory is empty
            print("Deleting", os.path.join(root, name))
            # print("This is the command to delete for testing deletions :", os.path.join(root, name))
            if os.rmdir(os.path.join(root, name)):
                print('Successfully deleted', os.path.join(root, name))




