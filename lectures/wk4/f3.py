import string  # importing a .py file to use its variables and methods
import random



print(string.digits)
print(  string.capwords("hello world", "-")   )

for i in range(5):
    print(random.randint(1, 11))


values = list(range(1, 21))

random_value = random.choice(values)

print(random_value)