# continually ask the user for an age, until they enter an odd age
age = 0
while age % 2 != 1:
    age = int(input("Enter an odd age: "))
    if age % 2 == 0:
        print("Sorry, but", age, "is not an odd age")
print("Thank you for your input")