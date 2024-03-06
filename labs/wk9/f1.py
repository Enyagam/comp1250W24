import string
"""
Ask the user for
    name
    address
    city
    country
    postal code

    use regex to validate input
"""
import re

def validate_name_non_regex():
    name1 = "Ben"
    name2 = "Ben Blanc"
    name3 = "Ben Prof Blanc"

    # split name value by space
    parts = name1.lower().split(" ")
    for part in parts:
        # 'ben' 'blanc' 'prof'
        for letter in part:
            if letter in "abcdefghijklmnopqrstuvwxyz": #string.ascii_lowercase:
                print("good letter")
            else:
                print("bad letter")
                return False


def validate_data(data, regex):
    """
    This is going to validate our user input
    :param title: Name of the data
    :param regex: Regex to test
    :param data:  string data to pass to the regex
    :return: boolean if data is valid
    """
    return True if re.match(pattern=regex, string=data, flags=re.I) else False


def main():
    print("Welcome to our wk9 program")
    answer = input("Would you like to run the program? y/n: ").lower().strip()[0]
    if answer == "y":
        run()


def run():
    name = input("Enter name: ")
    address = input("Enter address: ")
    postal_code = input("Enter postal code: ")

    regex_name = r"([a-zA-Z]+\s?){1,}"  # 'ben' 'ben ', 'ben blanc' 'ben prof blanc'

    regex_address = r"\d{1,}\s[a-zA-Z-]+\s(st|ave|rd|cres|ln|court|blvd|ci|dr|park)"

    regex_postal_code = r"[a-z][0-9][a-z]\s?[0-9][a-z][0-9]"  # LNL space or no space NLN


    # 160 kendal ave

    if not validate_data(name, regex_name):
        print("Invalid Name entered")
    if not validate_data(address, regex_address):
        print("Invalid Address entered")
    if not validate_data(postal_code, regex_postal_code):
        print("Invalid Postal entered")


if __name__ == '__main__':
    main()