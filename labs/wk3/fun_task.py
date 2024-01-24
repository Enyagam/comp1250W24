"""
ask the user to enter a
    season
    temperature

based on that
    output what coat the person should wear

Examples
    winter
    0
    wear a warm sweater

    winter
    -10
    light winter jacket

    winter
    -20 or lower
    warm winter jacket

"""

season = input("Enter a season: ")

# validate if season if winter, spring, summer, fall, autumn

acceptable_seasons = "winter spring summer fall autumn".split(" ")
print(acceptable_seasons)

if season not in acceptable_seasons:
    print("Sorry message")
else:
    print("continuing")

print()

if season in acceptable_seasons:
    pass
else:
    print(f"Sorry but {season} is not an acceptable season")


if season == "winter" or season == "spring" or season == "summer" or season == 'fall' or season == "autumn":
    pass
else:
    print("Sorry message")