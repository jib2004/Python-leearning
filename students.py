import  csv
# with open("students.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")

# with open("students.csv") as file:
#     for line in file:
#         name,house = line.rstrip().split(",") # -> Knowing this is returning two variables
#         print(f"{name} is in {house}")

students = []

# with open("students.csv") as file:
#     for line in file:
#         name,house = line.rstrip().split(",") # -> Knowing this is returning two variables
#         student = {}
#         student["name"] = name
#         student["house"] = house
#         students.append(student)


# CSV Library
# with open("students.csv") as file:
#     reader = csv.reader(file) -> returns list
#     for name,home in reader:
#         students.append({"name": name, "home": home})

# with open("students.csv") as file:
#     reader = csv.DictReader(file) # -> returns dictionary
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})


name = input("Enter student name: ")
home = input("Enter home address: ")

# with open("students.csv","a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name,home])

with open("students.csv","a") as file:
    writer = csv.DictWriter(file,fieldnames=["name","home"])
    writer.writerow({"name":name,"home":home})

# def get_name(student):
#     return student["name"]

# def get_house(student):
#     return student["house"]


# for student in sorted(students, key=get_name,reverse=True):
#     print(f"{student['name']} is in {student['house']}")

# for student in sorted(students, key=get_name):
#     print(f"{student['name']} is in {student['house']}")

# for student in sorted(students, key=lambda student:student["name"]):
#     print(f"{student['name']} is in {student['home']}")

