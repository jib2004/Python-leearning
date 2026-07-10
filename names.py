# names = []
#
# for _ in range(3):
#     names.append(input("What's name?: "))
#
# print(sorted(names))
#
# for name in sorted(names):
#     print(f"hello, {name}")


# name = input("What's your name?: ")
# print(f"Hello, {name}!")


# name = input("What's your name?: ")
# file = open("names.txt","w") # -> write
# file = open("names.txt","a") # -> append
# file.write(f"{name}\n")
# file.close()

# with open("names.txt","a") as file: #automatically closes file
#     file.write(f"{name}\n")

# with open("names.txt","r") as file:
#     lines = file.readlines()
#
# for line in lines:
#     print("hello, " + line.rstrip())

names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
    


