import os
"""
Hello everyone
This is a test file content
End of file
"""
for file in os.listdir("."):
    print(file)
    if file.endswith(".txt"):
        os.remove(file)
