name = "Introduction to Programming"
code = "comp1250"
students = list()
assignments = ["assignment1", "assignment2", "assignment3", "assignment4"]
grades = dict.fromkeys(assignments)


def get_student(index):
    return students[index]


def get_assignment_grade(assignment):
    if assignment in grades:
        return grades[assignment]
