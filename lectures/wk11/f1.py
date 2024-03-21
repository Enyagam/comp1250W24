f = open("test_file.txt")
print(f)
print(f.mode, f.closed, f.name)

print("*" * 20)
# read()            return str, retrieve all file content
# readline()        return str, retrieve one line at a time
# readlines()       return list, retreive all file content. each index = line


# all_content = f.read()
# print(all_content)
first_20_chars = f.read(20)
print(first_20_chars)
next_10_chars = f.read(10)
print(next_10_chars)
rest_of_file = f.read()
print(rest_of_file)