"""
Student-Course-Folder-Organizer

Ask the user for their School Name
Ask the user for their school year
Ask the user for their school semester

Create dirs School Name/year/semester

Ask student how many courses they are taking
In loop
    Ask student course code for each course
        Create directory & grades.txt file (empty)
"""
import os
import re
import sys
import time

school_name = input("Enter school name: ")
year = input("Enter school year: ")
semester = input("Enter the semester (fall, winter, spring): ")

if re.match(pattern=r'[a-zA-Z\s]+', string=school_name, flags=re.IGNORECASE):
    print("Good school name")

    if re.match(pattern=r'\d{4}', string=year):
        print("Good year")

        if semester.lower() in "fall winter spring".split(" "):
            print("Good semester")
            root_path = f"{school_name}/{year}/{semester}/"
            os.makedirs(root_path)

            course_count = int(input("How many courses are you taking? "))
            for i in range(1, course_count + 1):
                course_code = input("Enter the course code for course #" + str(i) + ": ")
                os.mkdir(root_path + course_code)
                open(root_path + course_code + "/grades.txt", 'w').close()

        else:
            print("Invalid semester", file=sys.stderr)

    else:
        print("Invalid year", file=sys.stderr)

else:
    print("Invalid school name", file=sys.stderr)

time.sleep(1)
print("Thank you for using our program")
