import random

class Hat:
    houses = ["Lagos", "Ikoyi", "Yaba"] # class variables

    @classmethod
    def sort(cls,name):
        house = random.choice(cls.houses)
        print(name, "is in", house)


# hat = Hat() no need to instantiate Hat() again because of @classmethods
Hat.sort("Harry")