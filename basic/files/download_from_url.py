"""
To run this file, need to install requests to your virtual environment

$ pip install requests

Download an image from a hardcopy url using two methods:
write method of files library to manage small content
copyfileobj method of shutil library to manage large content

Then the second option is added to another file and is imported
as a utility function
"""
import os
import requests
import shutil

from download_util import (
    download_file, download_file_smaller, download_file_slower
)

THIS_FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(THIS_FILE_PATH)
DOWNLOADS_DIR = os.path.join(BASE_DIR, "downloads")
os.makedirs(DOWNLOADS_DIR, exist_ok = True)

#url = "https://image.winudf.com/v2/image/Ym9tYmZpZ2h0ZXIuYWJvbWJlcm1hbmdhbWUuZnJlZWRvd25sb2FkMjAxODE5X3NjcmVlbl8wXzE1MjI0NTQ1NzRfMDMy/screen-0.jpg?fakeurl=1&type=.jpg"
url = "https://i.ytimg.com/vi/yvicDbCfrVo/maxresdefault.jpg"

# Call the best utility funcion from download_util file
download_file(url, DOWNLOADS_DIR)

# Call the utility funcion to download a smaller file
download_file_smaller(url, DOWNLOADS_DIR)

# Another function to download a file by chunks (more slower than the lastest two)
download_file_slower(url)