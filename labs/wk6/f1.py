import course

course.add_student("12345", "john", "smith")
course.add_student_grade("12345", "assignment1", 90)

student1 = course.get_student_by_id("12345")
print(student1)
print(course.get_student_grade("12345", "assignment1"))
