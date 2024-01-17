"""
ask the user for two numbers.
product the sum of those numbers
use string formatting
"""
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

result = num1 + num2
output = f"{num1} + {num2} = {result}" + "\n" * 2
print(f"{num1} + {num2} = {result}")
print(output)



mystery = f"{num1} + {num2} = {result}" + "\n" * 2
print(mystery)