name = "Intro to Programming"
code = "comp1250"
students = dict()
assignments = "assignment1 assignment2 assignment3 assignment4".split(" ")


def add_student(student_id, first_name, last_name):
    students[student_id] = {"first_name": first_name,
                            "last_name": last_name, "grades": dict()}


def get_student_by_id(student_id):
    # if student_id in students:
    #     return students[student_id]
    # else:
    #     return None
    return students[student_id] if student_id in students else None


def is_assignment_valid(assignment):
    return assignment in assignments


def add_student_grade(student_id, assignment, grade):

    if student_id in students and is_assignment_valid(assignment):
        students[student_id]["grades"][assignment] = grade


def get_student_grade(student_id, assignment):
    student = get_student_by_id(student_id)
    if student and is_assignment_valid(assignment):
        return student["grades"][assignment]
