info = [{'student': ['123', 'joe', 'smith'], 'grades': [{'Course Code': 'comp1255', 'Grade': '95'}, {'Course Code': 'comp1240', 'Grade': '95'}]}, {'student': ['234', 'mary', 'brown'], 'grades': [{'Course Code': 'comp1231', 'Grade': '98'}, {'Course Code': 'comp1255', 'Grade': '95'}]}]



share_course = []
share_grade = []

compared_combo = list()

for entry in info:
    for compare in info:
        c1 = entry["student"][0]
        c2 = compare["student"][0]
        if entry["student"][0] == compare["student"][0] or f"{c1}-{c2}" in compared_combo or f"{c2}-{c1}" in compared_combo:
            continue # same student
        compared_combo.append(c1 + "-" + c2)
        for courses_entry in entry["grades"]:
            for courses_compare in compare["grades"]:
                print(courses_entry, courses_compare)
                if courses_entry['Course Code'] == courses_compare['Course Code']:
                    share_course.append([entry, compare])
                if courses_entry['Grade'] == courses_compare['Grade']:
                    share_grade.append([entry, compare])

print("*" * 20)
print(share_course)
print(share_grade)