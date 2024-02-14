import course

course_name = course.name
print(course_name)
course.name = "comp1234"
print(course.name)

course.students.append(12345)
course.students.append(98765)
course.students.append(32468)

print(course.get_student(2))

course.grades["assignment1"] = 80

print(course.get_assignment_grade("assignment1"))
