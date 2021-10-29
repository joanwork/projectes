import os
import shutil
import logging

TO_LOGS = '00-Logs'
TO_IMAGES = '01-Images'
TO_VIDEOS = '02-Videos'
TO_EXE = '03-Executables'
TO_ISO = '04-Iso'
TO_OFFICE = '05-Office'
TO_ZIP = '06-Zip'
TO_TXT = '07-Txt'
TO_JAR = '08-Java'

folder_to_sort = os.getcwd()   #  path.expanduser('~Downloads')
file_list = os.listdir(folder_to_sort)


def move_file_to(file_path, folder_dest):
    print('***************************')
    if not os.path.exists(folder_dest):
        os.mkdir(folder_dest)

    base, extension = os.path.splitext(file_path)
    basename = os.path.basename(file_path)
    dest_file = os.path.join(folder_dest, basename)
    base2, extension2 = os.path.splitext(basename)

    i = 0
    while os.path.exists(dest_file):
        dest_file = os.path.join(folder_dest, base2 + f'_{i:03}' + extension)
        i = i + 1
    print('From: ' + file_path)
    print('To: ' + dest_file)
    shutil.move(file_path, dest_file)


for file in os.listdir(folder_to_sort):
    if file.lower().endswith((".jpg", ".gif", ".jpeg", "bmp", ".png")):
        file_path = os.path.join(folder_to_sort, file)
        move_file_to(file_path, os.path.join(folder_to_sort, TO_IMAGES))
    elif file.lower().endswith((".mp4", ".avi", ".mpg", "mpeg")):
        file_path = os.path.join(folder_to_sort, file)
        move_file_to(file_path, os.path.join(folder_to_sort, TO_VIDEOS))
    elif file.lower().endswith((".exe", ".com", ".msi")):
        file_path = os.path.join(folder_to_sort, file)
        move_file_to(file_path, os.path.join(folder_to_sort, TO_EXE))
    elif file.lower().endswith((".iso")):
        file_path = os.path.join(folder_to_sort, file)
        move_file_to(file_path, os.path.join(folder_to_sort, TO_ISO))
    elif file.lower().endswith((".doc", ".xls", ".xlsx", ".docx",".pdf", ".pptx")):
        file_path = os.path.join(folder_to_sort, file)
        move_file_to(file_path, os.path.join(folder_to_sort, TO_OFFICE))
    # the only startswith of the project
    elif file.lower().startswith(("securemedias")):
        file_path = os.path.join(folder_to_sort, file)
        move_file_to(file_path, os.path.join(folder_to_sort, TO_LOGS))
    elif file.lower().endswith((".zip", ".7z", ".rar", ".tgz")):
        file_path = os.path.join(folder_to_sort, file)
        move_file_to(file_path, os.path.join(folder_to_sort, TO_ZIP))
    elif file.lower().endswith((".csv", ".txt", ".me", ".ini")):
        file_path = os.path.join(folder_to_sort, file)
        move_file_to(file_path, os.path.join(folder_to_sort, TO_TXT))
    elif file.lower().endswith((".jar", ".java")):
        file_path = os.path.join(folder_to_sort, file)
        move_file_to(file_path, os.path.join(folder_to_sort, TO_JAR))
		


