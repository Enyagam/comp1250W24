person = {"firstname": "ben", "lastname": "blanc", "age":20}
print(person['firstname'])
print(person['lastname'])
print(person['age'])

print("age" in person)  # True
print("ben" in person.values())
for key in person.keys():
    print(key, person[key])
print("*" * 20)
for value in person.values():
    print(value)
print("*" * 20)
for key, value in person.items():
    print(key, value)
