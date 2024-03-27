import csv

keys = ["StudentID", "First Name", "Last Name"]

with open("my1.csv") as file:
    reader = csv.DictReader(file)
    # read object: automatically converts the content into a dictionary
    print(reader)
    for row in reader:
        print(row)
        print("Column 1 = ", row['StudentID'], row[keys[0]])
        print("Column 2 = ", row['First Name'], row[keys[1]])
        print("Column 3 = ", row['Last Name'], row[keys[2]])