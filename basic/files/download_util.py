"""
To run this file, need to install requests to your virtual environment

$ pip install requests

Build in functions to download a file. Use string and secrets to set a
name to new file 
"""
import os
import requests
import shutil
import string
import secrets

# Efficient function to download a file
def download_file(url, directory, fname=None):
    if fname == None:
        fname = os.path.basename(url)
    dl_path = os.path.join(directory, fname)

    # Using shutil to download large files, on efficient way
    with requests.get(url, stream=True) as r:
        with open(dl_path, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    return dl_path

# Function to download a smaller file
def download_file_smaller(url, directory, fname=None):
    if fname == None:
        # Make a new random name to the image
        alphabet = string.ascii_letters
        fname = ''.join(secrets.choice(alphabet))
        alphabet = alphabet + string.digits
        fname = fname.join([''.join(secrets.choice(alphabet) for i in range(3)), '.jpg'])
    dl_path = os.path.join(directory, fname)
    # To download a smallish item
    r = requests.get(url, stream=True)
    # Check if the request status code is 200 or rase an error
    r.raise_for_status()
    with open(dl_path, 'wb') as f:
        # Write in the file the content of the requested url
        f.write(r.content)
    return dl_path

# Another example
def download_file_slower(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parammeter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk: #filter out keep-alive new chunks
                    f.write(chunk)
                    # f.flush()
    return local_filename