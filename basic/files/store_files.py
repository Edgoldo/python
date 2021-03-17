"""
Check folder and files existence or create them
"""
import os

# Save in a macro the absolute route to this folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Save a path to a nonexistent folder called texts
files_dir = os.path.join(BASE_DIR, "texts")

# Check the existence of a folder 
if not os.path.exists(files_dir):
    print("This is not a valid path")

# Create a folder in path provided if not exist
os.makedirs(files_dir, exist_ok=True)

my_images = range(0, 2)

for i in my_images:
    fname = f"{i}.txt"
    file_path = os.path.join(files_dir, fname)
    if os.path.exists(file_path):
        print(f"Skipped {fname}")
        continue
    with open(file_path, 'w') as f:
        f.write("Text of this file {}".format(i))