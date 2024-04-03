import sys
file = "notes.txt"
try:
    f = open(file + "1", "r")
    print(f.read(10))
except FileNotFoundError as e:
    print(e, file=sys.stderr)
finally:
    try:
        f.close()
    except NameError:
        print("Process cannot be completed")
