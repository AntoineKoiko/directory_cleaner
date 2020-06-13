#!/bin/env python3

import os
from folderModule import Folder

#paht of folder we want to clean
folder_path = "/home/antoine.couacault/Downloads"

if not os.path.isdir(folder_path):
    print("Error : bad folder path : ", folder_path, ", is not a directory")
    quit(84)

#folder to clean the main folder:
sub_folders = {
                1 : {
                    "name" : "img",
                    "ext" : [".jpg", ".png"]
                    },
                2 : {
                    "name" : "text",
                    "ext" : [".txt", ".pdf"]
                    },
                3 : {
                    "name" : "code",
                    "ext" : [".c", ".py", ".dart", ".js", ".html", ".css", ".sh", ".h", ".yml"]
                    },
                4 : {
                    "name" : "compressed",
                    "ext" : [".zip", ".targz", ".xz", ".gz"]
                    },
                5 : {
                    "name" : "docs",
                    "ext" : [".doc", ".docx", ".xlsx"]
                    },
                6 : {
                    "name" : "undefined",
                    "ext" : [None]
                    }
            }

def get_sub_paht(main_path, sub_name):
    sub_path = main_path
    if main_path[len(main_path) - 1] != '/':
        sub_path += "/"
    sub_path += sub_name
    return sub_path

#initialize the folder we want to clean
main_dir = Folder()
main_dir.set_path(folder_path)
main_dir.obtain_content()

#check if subfolders exist and create itelse
for key in sub_folders:
    folder = sub_folders[key]
    folder['object'] = Folder()
    folder['object'].set_path(get_sub_paht(folder_path, folder['name']))
    if not folder['object'].is_existing_in(main_dir, folder['name']):
        folder['object'].create()

main_dir.obtain_content()


#sort file
main_dir.pop_dir_in_content()

for idx, entry in enumerate(main_dir.content):
    folder_find = False
    extension = main_dir.get_extension(entry)
    for key in sub_folders:
        sub = sub_folders[key]
        if extension in sub['ext']:
            main_dir.mv_file(entry, sub['object'])
            folder_find = True
    if not folder_find:
        main_dir.mv_file(entry, sub_folders[6]['object'])