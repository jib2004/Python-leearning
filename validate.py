import re
email = input("Enter your email address? ").strip()

# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")

# username,domain = email.split("@")
#
# if (username) and ("." in domain):
#     print("Valid")
# else:
#     print("Invalid")


# if re.search(".*@.*",email):
#     print("Email Address is valid")
# else:
#     print("Email Address is invalid")

# if re.search("..*@..*",email):
#     print("Email Address is valid")
# else:
#     print("Email Address is invalid")

# if re.search(".+@.+",email):
#     print("Email Address is valid")
# else:
#     print("Email Address is invalid")

# if re.search(r".+@.+\.edu",email):
#     print("Email Address is valid")
# else:
#     print("Email Address is invalid")

# if re.search(r"^.+@.+\.edu$",email):
#     print("Email Address is valid")
# else:
#     print("Email Address is invalid")

# if re.search(r"^.+@.+\.edu$",email):
#     print("Email Address is valid")
# else:
#     print("Email Address is invalid")

# if re.search(r"^[^@]+@[^@]+\.edu$",email):
#     print("Email Address is valid")
# else:
#     print("Email Address is invalid")

# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$",email):
#     print("Email Address is valid")
# else:
#     print("Email Address is invalid")

# if re.search(r"^\w+@\w+\.edu$",email): # \w any word character
#     print("Email Address is valid")
# else:
#     print("Email Address is invalid")

# if re.search(r"^\w+@\w+\.(com|edu|gov|net)$",email): # \w any word character
#     print("Email Address is valid")
# else:
#     print("Email Address is invalid")

if re.search(r"^\w+@\w+\.(com|edu|gov|net)$",email,re.IGNORECASE): # \w any word character
    print("Email Address is valid")
else:
    print("Email Address is invalid")