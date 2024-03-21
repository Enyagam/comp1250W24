f = open("test_file.txt", "w") # w => overwriting
# sets the file length to 0 => removes all file content

f.write("Hello world\nWriting content is fun\n")
for num in range(5):
    f.write(f"Writing Line {num}\n")
