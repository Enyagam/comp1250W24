import sys

try:
    print(1 + "hello")
    print("finished")
except:
    print("Error Occurred", file=sys.stderr)

print("How are you doing today")
