import re

name = input("Enter your name: ").strip()
# matches = re.search(r"^(.+), (.+)$",name)
# if matches:
#     last,first = matches.groups()
#     name = last+", "+first
#
# print(name)

if matches := re.search(r"^(.+), (.+)$",name):
    name = matches.groups(2) + " " + matches.groups(1)

print(name)