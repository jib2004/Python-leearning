class Student:
    def __init__(self, name, house, pet,age=None): # Initialization function -> Made age optional
        # if not name:
        #     raise ValueError("Student name cannot be empty")
        # if house not in ["Lagos", "Ikoyi", "Yaba"]:
        #     raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.age = age
        self.pet = pet

    def __str__(self): #-> this helps python print the class attr as a string if not provided it generates a code
        return f"{self.name} from {self.house} is {self.age}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Student name cannot be empty")
        self._name = name

    # Getter
    @property # to tell python to treat this as a getter
    def house(self):
        return self._house

    # Setter
    @house.setter #to tell python this is a setter
    def house(self, house):
        if house not in ["Lagos", "Ikoyi", "Yaba"]:
            raise ValueError("Invalid house")
        self._house = house


    # def charm(self):
    #     match self.pet:
    #         case "dog":
    #             return "dog"
    #         case "cat":
    #             return "cat"
    #         case "otter":
    #             return "otter"
    #         case _: #default
    #             return "unknown"


def main():
    student = get_student()
    print(student)


def get_student():
    # student = Student()
    name = input("Enter name: ")
    house = input("Enter house: ")
    age = input("Enter age: ")
    pet = input("Enter pet: ")
    return Student(name, house,pet,age)
    # try:
    #     return Student(name, house)
    # except ValueError:
    #     print("Invalid input")





# def main():
#     name,house = get_student()
#     student = get_student()
#     # student[1] ="Home" -> Tuples do not support this
#     print(f"{name} from {house}")
#     print(f"{student[0]} from {house[1]}")


# def get_student():
#     name = input("Enter your name: ")
#     house = input("Enter your house: ")
#     return name,house # Tuple -> is immutable meaning values can not be changed after assigned
"""
Lists are mutable
fruits = ["apple", "banana", "cherry"]
fruits[0] = "pear"
print(fruits) -> result: ["pear", "banana", "cherry"]

Dict is mutable
userInfo["name"] = "Wonder"
userInfo["age"] = 25
print(userInfo) -> result: 
{
    "name": "Wonder",
    "age": 25,
}

Tuple is immutable has shown above

"""



if __name__ == "__main__":
    main()