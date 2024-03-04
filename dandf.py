import os
import shutil

#1
directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
all_items = os.listdir(path)
print("Directories:", directories)
print("Files:", files)
print("All directories and files:", all_items)

#2
specified_path = "specified/path"
existence = os.path.exists(specified_path)
readability = os.access(specified_path, os.R_OK)
writability = os.access(specified_path, os.W_OK)
executability = os.access(specified_path, os.X_OK)
print("Path exists:", existence)
print("Readable:", readability)
print("Writable:", writability)
print("Executable:", executability)

# 3
given_path = "given/path"
if os.path.exists(given_path):
    filename = os.path.basename(given_path)
    directory = os.path.dirname(given_path)
    print("Filename:", filename)
    print("Directory portion:", directory)

# 4
text_file_path = "path/to/text_file.txt"
with open(text_file_path, 'r') as file:
    lines = file.readlines()
    line_count = len(lines)
print("Number of lines in the text file:", line_count)

#5
list_to_write = ["apple", "banana", "cherry"]
output_file_path = "path/to/output_file.txt"
with open(output_file_path, 'w') as file:
    for item in list_to_write:
        file.write(item + '\n')

# 6
    for i in range(26):
    file_name = chr(ord('A') + i) + ".txt"
    with open(file_name, 'w') as file:
        file.write("This is file " + file_name)

# 7
source_file_path = "path/to/source_file.txt"
destination_file_path = "path/to/destination_file.txt"
shutil.copyfile(source_file_path, destination_file_path)

# 8
file_to_delete = "path/to/file_to_delete.txt"
if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print("File deleted successfully.")
else:
    print("File does not exist.")
  
