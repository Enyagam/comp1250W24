"""
Ask the user to input their favourite destinations (city) for each time of the year
    winter
    summer
    spring
    fall
    
Store this information
    validate that each input is at least 3 characters

"""

# enter your fav destination of {season}
seasons = "winter summer spring fall".split(" ")
destination = ""

destinations = list()
destinations_by_season = dict()

for season in seasons:
    while len(destination) < 3:
        destination = input("Enter your favourite destination for " + season)
        if len(destination) >= 3:
            print("Thank you for inputting a valid destination value for", season)
            destinations.append(destination)
            destinations_by_season[season] = destination
        else:
            print("Sorry but", destination, "is invalid. Please try again")
    print("You entered", destination, "for the season of", season)
    destination = ""

print(destinations_by_season)
print(destinations)
print("Are there any duplicate values?")
print(len(destinations) != len(set(destinations)))
