"""
JPEG to PNG Convertor

1. sys module to take 2 arguments for the script
2. pathlib/os module to check if a folder exists
3. loop through the folder to grab images and convert them to png
4. save the files

"""

import os
import sys

input_folder_path = sys.argv[1]
# input_folder_path = "sample-images"
# input_folder_path = "D:\Repositories\image-processing-playground\sample-images"

# for root, dirs, files in os.walk(input_folder_path):
#     for file in files:
#         # append the file name to the list
#         file_list.append(os.path.join(root, file))

files_list = os.listdir(input_folder_path)

# test -> print all the file names
# for name in files_list:
#     print(name)
