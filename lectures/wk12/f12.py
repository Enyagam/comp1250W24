import os
import zipfile

with zipfile.ZipFile("my1.zip", "w") as file:
    for item in os.listdir("."):
        file.write(item)
print("Zip file was created")