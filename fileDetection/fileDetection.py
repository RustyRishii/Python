import os

file_path = "/Users/rishikeshbidkar/projects/welcome.py"

if os.path.isfile(file_path):
    print("Yes, it's a file")
else:
    print("No it's not a file")
