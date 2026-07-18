# Inheritance
class Wizard:
    def __init__(self,name):
        if not name:
            raise ValueError ("Missing name")
        self.name = name

        ...

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)#To inherit name from wizard
        self.house = house

        ...

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

        ...

wizard = Wizard("Jimmy")
student = Student(f"Harry","Yaba")
professor = Professor("John", "Biology")