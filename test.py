import random
import statistics
import sys
import json
import cowsay
import requests

# from random import choice

# def main():
#     aCounter(5)
#     mCounter(5)
#
# def aCounter(a):
#     for i  in range(a):
#         i+=1
#         print("*" * i)
#         a -=1
#
#
# def mCounter(n):
#     for i in range(1, n + 1):        # i goes 1, 2, 3, ..., n
#         row = ""
#         for j in range(1, i + 1):    # j goes 1 up to i
#             row += str(i * j) + " "  # build the row as a string
#         print(row.strip())           # print the whole row at once
# main()

# students = ["Mario","Luigi","Bowser","Peach"]
# for i in range(len(students)):
#     print(i,students[i],end=",")
#
# # dict -> Key-value pairs
# students2 ={
#     "Mario":"Mario's Circuit",
#     "Luigi":"Luigi Circuit",
#     "Bowser":"Bowser Castle",
#     "Peach":"Peach Palace",
#     "toad":{
#         "car":"Beach Buggy",
#         "house":"Toads Road"
#     }
# }
#
# print("\n",students2["Mario"],sep="")
# print(students2["Luigi"])
# for student in students2:
#     print(student,students2[student],sep=":")
#
# students3 = [
#     {"name":"John","age":28,},
#     {"name":"Michael","age":21,},
#     {"name":"James","age":22,},
#     {"name":"Robert","age":23,},
#     {"name":"Mark","age":None,}
# ]
#
# for student in students3:
#     print(student["name"],student["age"],sep=" -> ")

# Random

# coin = random.choice(["heads","tails"])
# coin = choice(["heads","tails"])
# print(coin)
# number = random.randint(1, 10)
# print(number)

# cards = ["jack", "queen", "king", "ace"]
# random.shuffle(cards)
# print(cards)

# print(statistics.mean([1,2,3,4,5]))
# print(statistics.median([1,2,4,5]))
# print(statistics.mode([1,2,3,4,5]))

# print("hello, my name is ", sys.argv[1])
"""
-> python test.py Jibola
-> hello, my name is  Jibola
"""

# cowsay package -> pip install cowsay
# if len(sys.argv) == 2:
#     # cowsay.cow("hello, " + sys.argv[1])
#     cowsay.trex("hello, " + sys.argv[1])

# requests -> to make web requests
if len(sys.argv) != 2:
    sys.exit() # can have text in it

response = requests.get("https://itunes.apple.com/search?entity=song&limit=3&term="+sys.argv[1])
# print(json.dumps(response.json(),indent=2))# Helps you indent it and manipulate json
o = response.json()
for result in o["results"]:
    print(result["trackName"])