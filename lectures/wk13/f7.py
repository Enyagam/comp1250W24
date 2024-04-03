# Purpose create our own errors?
# Whaaat? Why in the world would we want to do this?

# Asking the user to input a valid age.
# A valid age is an integer, 0-120
age = int(input("Enter an age between 0 and 120: "))

if age >= 0 and age <= 120:
    print("Entered valid age")
else:
    print("Entered invalid age")
print("Thank you for your input")
