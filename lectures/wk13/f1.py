import sys

try:
    print(1 + "hello")
    print("next statement")
except:
    print("Error Occurred", file=sys.stderr)
