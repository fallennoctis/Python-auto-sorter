import os
import shutil
import getpass
import configparser
from typing import List
# from tkinter import Tk
from tkinter.filedialog import askdirectory

User = getpass.getuser()
path = ('C:/Users/' + User + '/Downloads/')
subPath = (path + 'Documents/')
names = os.listdir(path)
subNames = os.listdir(subPath)
folder_name: List[str] = ['Programs Installers', 'Books', 'Pics', 'Documents', 'AHK Scripts', 'RARs',
                          'Cheat tables', 'SC2 Banks and Replays']
folderSubNames: List[str] = ['Excels', 'Word', 'PDFs', 'Logs', 'Text Files', 'Power Points']

#                fileExtension: 'locations'
fileTypeDict = {"exe": 'Programs Installers/',
                "msi": 'Programs Installers/',
                "jar": 'Programs Installers/',
                "epub": 'Books/',
                "png": 'Pics/',
                "jpg": 'Pics/',
                "ahk": 'AHK Scripts/',
                "rar": 'RARs/',
                "zip": 'RARs/',
                "7z": 'RARs/',
                "ct": 'Cheat tables/',
                "xlsx": 'Documents/Excels/',
                "xlsm": 'Documents/Excels/',
                "csv": 'Documents/Excels/',
                "doc": 'Documents/Word/',
                "pdf": 'Documents/PDFs/',
                "log": 'Documents/Logs/',
                "ppt": 'Documents/Power Points/',
                "txt": 'Documents/Text Files/'
                }

if os.path.exists(path) is False:
    if os.path.exists("Auto_sorter_configfile.ini"):
        config_obj = configparser.ConfigParser()
        config_obj.read("Auto_sorter_configfile.ini")
        filLocation = config_obj['File Location']
        path = filLocation["path"]
        subPath = filLocation["subPath"]
    else:
        print(f'Unable to locate folder {path}')
        path = askdirectory(title='Select Your Downloads folder')
        path = str(path + "/")
        subPath = (path + 'Documents/')
        config = configparser.ConfigParser()
        config.add_section('File Location')
        config.set('File Location', 'path', path)
        config.set('File Location', 'subPath', subPath)
        try:
            with open("Auto_sorter_configfile.ini", 'w') as configfile:
                config.write(configfile)
        except PermissionError as err:
            print(err)

for fol_nam in folder_name:
    if not os.path.exists(path + fol_nam):
        os.makedirs(path + fol_nam)

for fol_nam in folderSubNames:
    if not os.path.exists(subPath + fol_nam):
        os.makedirs(subPath + fol_nam)

for file_name in names:
    files = file_name.lower().split(".")[-1]
    x = 1
    if files in fileTypeDict.keys():
        locations = fileTypeDict.get(files)
        if os.path.exists(path + locations + file_name):  # file is in location
            fileVar = file_name.split(".")
            file_name2 = str(fileVar[0]) + "(" + str(x) + ")" + "." + str(files)
            while True:
                if os.path.exists(path + locations + file_name2):  # file is in location
                    fileVar = file_name.split(".")
                    x += 1
                    file_name2 = str(fileVar[0]) + "(" + str(x) + ")" + "." + str(files)
                else:
                    try:
                        shutil.move(path + file_name, path + locations + file_name2)
                    except PermissionError as err:
                        print(err)
                    break
        else:
            try:
                shutil.move(path + file_name, path + locations + file_name)
            except PermissionError as err:
                print(err)
    elif file_name in folder_name or file_name in folderSubNames or file_name == "desktop.ini":
        pass
    else:
        print(f"{file_name} Not found")

for root, dirs, files in os.walk(path, topdown=False):
    for name in dirs:
        if len(os.listdir(os.path.join(root, name))) == 0:  # check whether the directory is empty
            print("Deleting", os.path.join(root, name))
            # print("This is the command to delete for testing deletions :", os.path.join(root, name))
            if os.rmdir(os.path.join(root, name)):
                print('Successfully deleted', os.path.join(root, name))
