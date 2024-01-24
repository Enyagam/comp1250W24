"""
you want to ask the user to input a temperature sub-zero degrees.
How do you enforce this value?
Answer: use an if statement, give the user a message as feedback
"""

temperature = float(input("Enter a sub-zero degree Celsius temperature: "))

if temperature < 0:
    print("Great! Thanks! You inputted the value of", temperature)
else:
    print(f"Sorry but {temperature} is not a sub-zero degree temperature")
