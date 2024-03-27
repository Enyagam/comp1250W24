import os
import zipfile
filename = "my1.zip"
with zipfile.ZipFile("my1.zip", "r") as file:
    if not os.path.exists("unzipped"):
        os.mkdir("unzipped")
    file.extractall(path="unzipped")

