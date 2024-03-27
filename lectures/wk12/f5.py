data = "StudentID,First Name,Last Name\n123,John,Doe\n456,Jane,Williams\n"
with open("my1.csv", "w") as file:
    file.write(data)

