import os
import shutil
from_dir = 'C:/Users/user/Desktop/C102/images'
to_dir = 'C:/Users/user/Desktop/Doc_files'
list_of_files = os.listdir(from_dir)
print(list_of_files)
for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    if extension == '':
        continue
    if extension in ['.txt', '.pdf', '.doc']:
        path1 = from_dir+'/'+file_name
        path2 = to_dir
        shutil.move(path1, path2)