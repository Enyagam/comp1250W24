import sys
# ask the user for an integer number
# thank the user or display an error
import time

try:
    num = int(input("Enter an integer number"))
    print("The number inputted was", num)
except ValueError as e:
    print(e, file=sys.stderr)
finally:
    time.sleep(1)
    # release resources
    print("Thank you for using our script")
