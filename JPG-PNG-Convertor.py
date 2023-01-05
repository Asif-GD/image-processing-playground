"""
JPEG to PNG Convertor

1. sys module to take 2 arguments for the script
2. pathlib/os module to check if a folder exists
3. loop through the folder to grab images and convert them to png
4. save the files

"""

import os
import sys
from PIL import Image

input_folder = sys.argv[1]
output_folder = sys.argv[2]
# input_folder_path = "sample-images"
# input_folder_path = "D:\Repositories\image-processing-playground\sample-images"
# print(input_folder_path)

files_list = os.listdir(input_folder)

# test -> print all the file names
# for file in files_list:
#     print(file)

# check if a folder exists, or else create it
if not os.path.exists(output_folder):
    os.mkdir(f"{output_folder}")

# loop through the directory and convert all jpeg files to png files
for file in files_list:
    sample_image = Image.open(f".\\{input_folder}{file}")
    only_file_name = os.path.splitext(file)
    sample_image.save(f".\\{output_folder}{only_file_name[0]}.png", format="PNG")
