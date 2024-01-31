# ask the user to enter there first and last name separated by a space

name = input("Enter your name")

# convert the name to firstname and lastname (two lists)

names = name.split(" ") # split() converts string to list, by seperator
print(names)
first_name = list(names[0])  # names[0]  => "Ben"   => convert to list ["B", "e", "n"]
last_name = list(names[1])

print(first_name, last_name)