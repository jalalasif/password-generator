# Password Generator Project. This program takes instructions on password specification and generates one
# This is a project in construction and will include a GUI in the future
import random

# Letters, numbers, and symbols to incorporate into the password
import string

# Letters, numbers and symbols to choose from, and a list to hold the assigned keys
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
pass_list = []

# User prompts
print("Welcome to the PyPassword Generator!")

# Assign letters
nr_letters = int(input("How many letters would you like in your password?\n"))
for i in range(nr_letters):
    r = random.choice(letters)
    pass_list.append(r)

# Assign symbols
nr_symbols = int(input(f"How many symbols would you like?\n"))
pass_symbols = ""
for i in range(nr_symbols):
    r = random.choice(symbols)
    pass_list.append(r)

# Assign numbers
nr_numbers = int(input(f"How many numbers would you like?\n"))
pass_numbers = ""
for i in range(nr_numbers):
    r = random.choice(numbers)
    pass_list.append(r)

# Combine into a shuffled password
random.shuffle(pass_list)
password = "".join(str(x) for x in pass_list)
print(f"Your password is: {password}")
