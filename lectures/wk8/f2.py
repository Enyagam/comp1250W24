import re
name = input("Enter your name: ")
number = input("Enter your number: ")


# use regex to determine if the name and name is correct:
pattern_name = r"[a-z]+"   # what is a valid name?

# questions to answer: are we allowing first and last names? NO

# does regex match the pattern starting from START of text/string
result = re.match(pattern=pattern_name, string=name, flags=re.I)
# Match object OR None
if result:
    print("Good jobs")
    # None objects was not returned
    print(result.string)  # return the string value passed to the match method
    start_index, end_index = result.span()

    print(result.span())
    print("Match started from index", start_index, "and ended at index", end_index)
    print(result.group())

    for hit in result.group():
        print(hit)
    if end_index == len(result.string):
        print("All characters matched")
    else:
        print("Some characters are invalid")
else:
    print("Invalid name")

print(f"Name={name}, Number={number}")

