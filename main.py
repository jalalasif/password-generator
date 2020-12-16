# Password Generator Project. This program takes instructions on password specification and generates one
# This is a project in construction and will include a GUI in the future
import random

# Letters, numbers, and symbols to incorporate into the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# User prompts
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Generates samples of random elements per user specifications
rand_letters = random.sample(letters, nr_letters)
rand_numbers = random.sample(numbers, nr_numbers)
rand_symbols = random.sample(symbols, nr_symbols)

# Combine into an ordered (unshuffled) password
str_pass = rand_symbols + rand_letters + rand_symbols

# Shuffle the password to break any predictability in structure and adjoin them into a string
random.shuffle(str_pass)
password = ''.join(str(elem) for elem in str_pass)
print(password)
