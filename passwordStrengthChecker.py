#3. Design a Password Strength Checker that evaluates a given password.

import re

def passwordCheck(inputPassword):

    length_check = len(inputPassword) >= 8
    character = re.search(r"[.?!@&]", inputPassword) is not None
    uppercase = re.search(r"[A-Z]", inputPassword) is not None
    lowercase = re.search(r"[a-z]", inputPassword) is not None
    number = re.search(r"[0-9]", inputPassword) is not None

    if length_check and character and uppercase and lowercase and number:
        print(" Strong password")
    else:
        print(" Weak password")

password = "Adithya@29"
passwordCheck(password)
