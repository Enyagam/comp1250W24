import re
number = input("Enter your number: ")  # 12345: 12 345, 12-34 5


pattern1 = r"[0-9]+"
pattern2 = r"\d+"

pattern3 = r"\s|-"
replace3 = r""
number = re.sub(pattern=pattern3, repl=replace3, string=number)

result = re.match(pattern=pattern1, string=number)
if result and result.span()[1] == len(number):
    print("Valid number")
else:
    print("invalid number")
