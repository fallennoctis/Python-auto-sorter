import configparser
#import getpass
import os
import shutil
import filecmp
from tkinter.filedialog import askdirectory

#User = getpass.getuser()
User = os.path.expanduser('~')
try:
    path = (User + '/Downloads/')
    subPath = (path + 'Documents/')
    names = os.listdir(path)
    subNames = os.listdir(subPath)
except FileNotFoundError as err:
    print(f'Unable to auto find your downloads folder! Error:{err}')
folderName = ['Programs Installers', 'Books', 'Pics', 'Documents', 'AHK Scripts', 'RARs', 'Audio and Video']
folderSubNames = ['Excels', 'Word', 'PDFs', 'Logs', 'Text Files', 'Power Points']

# Structure for the dictionary is as follows:
#                fileExtension: 'locations'
fileTypeDict = {"exe": 'Programs Installers/',
                "msi": 'Programs Installers/',
                "jar": 'Programs Installers/',
                "epub": 'Books/',
                "png": 'Pics/',
                "jpg": 'Pics/',
                "jfif": 'Pics/',
                "gif": 'Pics/',
                "ahk": 'AHK Scripts/',
                "rar": 'RARs/',
                "zip": 'RARs/',
                "7z": 'RARs/',
                "m4a": 'Audio and Video/',
                "mp3": 'Audio and Video/',
                "mp4": 'Audio and Video/',
                "wav": 'Audio and Video/',
                "xls": 'Documents/Excels/',
                "xlsx": 'Documents/Excels/',
                "xlsm": 'Documents/Excels/',
                "csv": 'Documents/Excels/',
                "doc": 'Documents/Word/',
                "docx": 'Documents/Word/',
                "pdf": 'Documents/PDFs/',
                "log": 'Documents/Logs/',
                "pptx": 'Documents/Power Points/',
                "txt": 'Documents/Text Files/',
                "rtf": 'Documents/Text Files/'
                }
# Check the normal file path and if not found allowing selection of it
if os.path.exists(path) is False:  # set true to pick your own location

    if os.path.exists("Auto_sorter_configfile.ini"):  # checks for the ini file and loads it
        config_obj = configparser.ConfigParser()
        config_obj.read("Auto_sorter_configfile.ini")
        filLocation = config_obj['File Location']
        path = filLocation["path"]
        subPath = filLocation["subPath"]
        names = os.listdir(path)
        subNames = os.listdir(subPath)
    else:  # if needed creates the file for the config
        print(f'Unable to locate folder {path}')
        path = askdirectory(title='Select Your Downloads folder')
        path = str(path + "/")
        subPath = (path + 'Documents/')
        names = os.listdir(path)
        subNames = os.listdir(subPath)
        config = configparser.ConfigParser()
        config.add_section('File Location')
        config.set('File Location', 'path', path)
        config.set('File Location', 'subPath', subPath)
        try:
            with open("Auto_sorter_configfile.ini", 'w') as configfile:
                config.write(configfile)
        except PermissionError as err:
            print(err)

for fol_nam in folderName:
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
        # print(f'{path} + {locations} + {file_name}')
        if os.path.exists(path + locations + file_name):  # file is in location
            if filecmp.cmp(path + file_name, path + locations + file_name, shallow=False) is False:
                fileVar = file_name.split(".")
                file_name2 = str(fileVar[0]) + "(" + str(x) + ")" + "." + str(files)
                while True:
                    if os.path.exists(path + locations + file_name2):  # if file is already there we need to rename it.
                        if filecmp.cmp(path + file_name, path + locations + file_name2, shallow=False) is False:
                            fileVar = file_name.split(".")
                            x += 1
                            file_name2 = str(fileVar[0]) + "(" + str(x) + ")" + "." + str(files)
                        else:
                            break
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
    elif file_name in folderName or file_name in folderSubNames or file_name == "desktop.ini":
        pass
    else:
        print(f"{file_name} Not found")

for root, dirs, files in os.walk(path, topdown=False):
    for name in dirs:
        if len(os.listdir(os.path.join(root, name))) == 0:  # check if directory is empty, if it is than delete it
            print("Deleting", os.path.join(root, name))
            if os.rmdir(os.path.join(root, name)):
                print('Successfully deleted', os.path.join(root, name))
