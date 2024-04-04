import os

file_path = "my_first_file.txt"

# Check if the file exists
if os.path.exists(file_path):
    # Delete the file
    os.remove(file_path)
    print("File deleted successfully!")
else:
    print("File already deleted!")
