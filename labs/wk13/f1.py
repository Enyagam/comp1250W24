"""
Asking using to enter a school name, school semester
    If either data is invalid, raise exception
"""
import sys


def get_school_name() -> str:
    name = input("Enter a school name: ")

    if len(name) < 3:
        raise ValueError(name + " is too short. Must be at least 3 characters")

    return name

def get_school_semester() -> str:
    semester = input("Enter the school semester: ").lower()
    options = "winter spring summer fall autumn".split(" ")
    if semester not in options:
        raise ValueError(f"{semester} is not a valid semester. Please choose between one of the following options {', '.join(options)}")

    return semester


def main():
    try:
        name = get_school_name()
        semester = get_school_semester()

        print(f"You attend {name.title()} for the {semester.title()} semester.")
    except ValueError as e:
        print(e, file=sys.stderr)


if __name__ == '__main__':
    main()
