"""
Ask the user for their name
Ask the user for their birth year
Output their name
AND
how old they are in
    years
    months
    weeks
    days

"""
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
year = 2024
print("Your name is", name)
print("You were born in", birth_year)
print(f"You are { year-birth_year } years old")
print(f"You are {(year-birth_year) * 12 } months old")
print(f"You are {(year-birth_year) * 52} weeks old")
print(f"You are {int(round( (year-birth_year) * 365.25, 0 ))} days old")





