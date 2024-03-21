f = open("test_file.txt")

first_line = f.readline()
print(first_line)
for line in f:
    print(line.rstrip())