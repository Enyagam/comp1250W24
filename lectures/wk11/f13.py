f = open("test_file.txt", "a+")  # primary to append but ALSO to read
r = f.read(5)
print(r)  # nothing or Hello
# how do I read contents from the beginning without changing the mode?
f.seek(0)
print(f.read(5))