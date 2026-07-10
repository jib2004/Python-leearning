# with open("students.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")

# with open("students.csv") as file:
#     for line in file:
#         name,house = line.rstrip().split(",") # -> Knowing this is returning two variables
#         print(f"{name} is in {house}")

students = []

with open("students.csv") as file:
    for line in file:
        name,house = line.rstrip().split(",") # -> Knowing this is returning two variables
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)

def get_name(student):
    return student["name"]

def get_house(student):
    return student["house"]


for student in sorted(students, key=get_name,reverse=True):
    print(f"{student['name']} is in {student['house']}")