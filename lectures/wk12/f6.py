import csv

with open("my1.csv") as file:
    reader = csv.reader(file)
    # read object: automatically converts the content into a list
    print(reader)
    for row in reader:
        print(row)
        print("Column 1 = ", row[0])
        print("Column 2 = ", row[1])
        print("Column 3 = ", row[2])