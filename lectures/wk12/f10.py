import csv
filename = "my2.csv"
field_names = "StudentID,Assignment,Grade"
data = [
    [12345, "assignment 1", 90],
    [654321, "assignment 2", 80],
    [456796, "assignment 1", 75],
    [46731, "assignment 2", 95],
    [13173, "assignment 3", 70],
]

# write data to a csv file
# NOT using CSV module
with open(filename, "w") as file:
    writer = csv.DictWriter(file, lineterminator='\n', fieldnames=field_names.split(","))
    writer.writeheader()  # write the fieldnames as the first line in the csv file
    writer.writerow({"StudentID": 12345, "Assignment": "Assignment 1", "Grade": 90})
    writer.writerow({"StudentID": 654321, "Assignment": "Assignment 2", "Grade": 80})
    writer.writerow({"StudentID": 456796, "Assignment": "Assignment 1", "Grade": 75})
    writer.writerow({"StudentID": 46731, "Assignment": "Assignment 2", "Grade": 95})
    writer.writerow({"StudentID": 13173, "Assignment": "Assignment 3", "Grade": 70})
