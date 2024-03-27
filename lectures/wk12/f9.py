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
    writer = csv.writer(file, lineterminator='\n')
    # writerows: pass in collection: list or tuple. normally list
    writer.writerow(field_names.split(','))  # header row
    writer.writerows(data)
