"""
From 30 Days of Python tutorial, made by Coding Entrepreneurs.

Day 10 - Files - Create, Read and Download

Working with files
"""
# Start with this basic commands, then:
# 1) Check file_manager.py
# 2) store_files.py
# 3) download_from_url.py

# Basic way to create, open and write in a file
file_name = "hello-text.txt"
file_object = open(file_name, 'w')
file_object.write("This is de first line")
file_object.close()

# Normally way to create, open and write a file. With open and close automatically the file
with open(file_name, 'w') as file_object:
    file_object.write("This is the normal way to write the first line in a file")

# Normally way to open and read a file
with open(file_name, 'r') as file_object:
    print(file_object.read())