"""
Create a script that will compare Student Grades

Ask the user how many students they would like to add to the program
    Each student, add: student id, firstname, lastname
        Add their grades
            course code
            grade
            continually ask until they enter a empty space

    Compare each student and determine
        students that share the same class
        students that share the same grade irregardless to course code
"""
number_of_students = int(input("Enter the number of students: "))
fields_student = "Student ID,First Name,Last Name".split(",")
fields_grade = "Course Code,Grade".split(",")

info = []

for entry in range(1, number_of_students + 1):
    student_data = list()
    for field in fields_student:
        student_data.append(input(f"Enter the {field} for student #{entry} of {number_of_students}"))
    grades = list()
    print()
    course_data = dict()
    while True:
        error = False
        for field in fields_grade:
            student_name = f"{student_data[1]} {student_data[2]}"
            data = input(f"Enter the {field} for the student {student_name}: ")
            if len(data) == 0:
                print("Invalid input. Exiting the program")
                error = True
                break
            course_data[field] = data
        print("You've successfully added the course for student", student_name)
        if not error:
            grades.append(course_data)
        answer = input("Would you like to enter another grade? y/n").lower()
        if "y" not in answer:
            info.append({"student": student_data, "grades":grades})
            break

share_course = []
share_grade = []

compared_combo = list()

for entry in info:
    for compare in info:
        c1 = entry["student"][0]
        c2 = compare["student"][0]
        if entry["student"][0] == compare["student"][0] or f"{c1}-{c2}" in compared_combo or f"{c2}-{c1}" in compared_combo:
            continue # same student comparison
        compared_combo.append(c1 + "-" + c2)
        for courses_entry in entry["grades"]:
            for courses_compare in compare["grades"]:
                if courses_entry['Course Code'] == courses_compare['Course Code']:
                    share_course.append([entry, compare])
                if courses_entry['Grade'] == courses_compare['Grade']:
                    share_grade.append([entry, compare])

print("*" * 20)
print(share_course)
print(share_grade)

