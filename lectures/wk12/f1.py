
text = "I love python"

print(text)
bytes = text.encode()
print(bytes)
convert = bytes.decode()
print(convert)

with open("my1.bin", "wb") as file:
    file.write(bytes)
