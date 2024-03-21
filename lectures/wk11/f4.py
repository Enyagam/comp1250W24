f = open("test_file.txt")
how_many = len(f.read())  # how many characters

f.seek(0)  # move cursor to a specific byte of the file

print(how_many)
f.read(10)
print(f.tell())  # where the cursor is in the file
f.readline()
print(f.tell())
