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

    input your conditions for
    summer, fall, spring

"""

season = input("Enter a season: ").lower()

# validate if season if winter, spring, summer, fall, autumn

acceptable_seasons = "winter spring summer fall autumn".split(" ")
print(acceptable_seasons)

if season not in acceptable_seasons:
    print(f"Sorry but {season} is not an acceptable season")
else:
    temperature = float(input("Enter a temperature: "))
    if season == "winter":
        if temperature >= 0:
            print("You should wear a warm sweater")
        elif temperature >= -10:
            print("You should wear a light winter jacket")
        elif temperature >= -20:
            print("You should wear a warm winter jacket")
    elif season == "summer":
        if temperature <= 10:
            print("You should wear a long sleeved t-shirt")
        elif temperature <= 20:
            print("You should wear a t-shirt")
        else:
            print("Stay indoors")
