import pickle
with open("my2.bin", "rb") as file:
    content = pickle.load(file)
    print(content.decode())

