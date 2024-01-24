season = input("Enter the season: ")

# output the temperature range based on season

"""
winter:
    0 to -50
spring
    0 - 19
fall
    0 - 10
summer
    20 - 35
"""
low = 0
high = 0
if season == "winter":
    low = -50
    high = 0
elif season == "spring":
    low = 0
    high = 19
elif season == "fall":
    low = 0
    high = 10
elif season == "summer":
    low = 20
    high = 35

print(f"The season of {season} has the temperature range of: Low= {low} & High = {high}")