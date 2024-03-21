f = open("test_file.txt", "a")

# lines = ["first line content", "second line content", "third line content"]
lines = ["first line content\n", "second line content\n", "third line content\n"]

# f.writelines(lines0

lines1 = [123, 45.68, "hi there", "you're awesome"]

for line in lines1:
    f.write(str(line) + "\n")
