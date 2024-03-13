"""
sys: info about the python environment
        standard input
        standard output
        arguments passed to the script
"""
import sys

print(sys.version)
# sys.exit("We're done here!")
print("This text is urgent", file=sys.stderr)  # text will be in red

print("Danger, danger", file=sys.stderr)

print(sys.argv[0])

# run a python file using the command line
