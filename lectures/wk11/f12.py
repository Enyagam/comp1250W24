import os

f = open("test_file.txt", "r+")  # primary to read but ALSO to write
# cursor starts at byte 0
# r = f.read(5)
# print(r)  # Hello
# f.write("Benny")
# how do I write to the end of the file without changing the mode
f.seek(3, os.SEEK_END)  # 3rd last character
f.seek(3)  # 3rd character
f.seek(0, os.SEEK_END)  # last char
f.write("Benny")

