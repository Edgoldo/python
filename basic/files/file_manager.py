"""
Working with system paths and files
"""
import os

# Get the absolute path to this file
this_file_path = os.path.abspath(__file__)
# Save the route to the folder that contains this file in a macro
BASE_DIR = os.path.dirname(this_file_path)
# Save the route to the folder parent of BASE_DIR
PARENT_BASE_DIR = os.path.dirname(BASE_DIR)

# Get a file from the current folder by a relative path
# email_txt = "templates/email.txt"

# Get a file by from a system path by a relative path
# email_txt = os.path.join("templates", "email.txt")

# Get a file from the absolute path
email_txt = os.path.join(BASE_DIR, "templates", "email.txt")

content = ""

with open(email_txt, 'r') as f:
    content = f.read()

print(content.format(name = "Full Name"))