import pickle

data = 'everyone loves python'.encode()
with open("my2.bin", "wb") as file:
    pickle.dump(data, file)

