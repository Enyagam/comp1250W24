# ask the user for two numbers
# create a list of int values from num1 to num2 (inclusive)

num1 = int(input("Enter a first number"))
num2 = int(input("Enter a second number"))

number_range = list(range(num1, num2 + 1))
print(number_range)

print("sum of these numbers is", sum(number_range))
print("avg of these numbers is", sum(number_range) / len(number_range))

does_exist = int(input("Enter a number to find in the list"))

if does_exist in number_range:
    print(does_exist, "was found at index", number_range.index(does_exist),
          "and occurs", number_range.count(does_exist), "times")
else:
    print(does_exist, "does not exist in the list")

to_add = int(input("Enter a number to add"))
if to_add not in number_range:
    number_range.append(to_add)
else:
    print("Sorry but", to_add, "was not added because it's already in the list")
