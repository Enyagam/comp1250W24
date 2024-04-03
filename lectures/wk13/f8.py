# Purpose create our own errors?
# Whaaat? Why in the world would we want to do this?

# Asking the user to input a valid age.
# A valid age is an integer, 0-120
import sys
from sys import stderr
try:
    age = int(input("Enter an age between 0 and 120: "))

    if age <= 0 or age > 120:
        raise ValueError(f"{age} value is invalid")

    print("You have entered the value of", age)

except ValueError as e:
    print(e, file=sys.stderr)
else:
    print(f"Age value of {age} is valid!")
finally:
    print("Thank you for your using our program")
