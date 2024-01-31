# ask the user to input their address
# store each part of there address in a list

street_number = int(input("Enter street number"))
street_name = input("Enter street name")
unit_number = int(input("Enter unit number"))

city = input("Enter city")
province = input("Enter province")
postal_code = input("Enter postal code")[:7]
country = input("Enter country")

address_info = [street_number, street_name, unit_number, city, province, postal_code, country]

# ask user to enter any text. Determine how many times this text occurs in address info
text = input("Enter any text")

counter = 0
for each_value in address_info:
    counter += str(each_value).count(text)

print(text, "was found", counter, "times in the address info")
