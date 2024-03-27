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
    file.write(field_names + '\n')
    for row in data:
        for column in row:
            file.write(f"{column},")
        file.write('\n')
