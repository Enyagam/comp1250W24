import sys
try:
    name = input("Enter your name: ")
    print(name)
    chars = list(name)  # transform name to a list
    index = int(input(f"Enter an index value between 0 "
                      f"and {len(chars) - 1}"))  # can result in exception
    print(f"The {index} index of the string '{name}' is {name[index]}")  # can result in exception

    d = dict()
    print(d['hello'])

    f = open(name, "r")  # Can result in an exception
    print("File Contents is " + f.read())
except KeyError as e:
    print("Key Error occurred", file=sys.stderr)
except ValueError as e:
    print("Invalid int number!", e, file=sys.stderr)
except IndexError as e:
    print("Index value of", index, "is out of bounds", file=sys.stderr)
except FileNotFoundError as e:
    print("Could not find the file", name, file=sys.stderr)
except Exception:
    print("I don't know what happened, but something went wrong", file=sys.stderr)