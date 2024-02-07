
while True:
    # print("This loop will never end")
    age = int(input("Enter your age"))
    if age > 0:
        break # stopping the loop
    print(age, "is not a valid age")
print("You are", age, "years old")