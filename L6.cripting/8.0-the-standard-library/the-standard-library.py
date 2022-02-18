'''The Standard Library
The Python Standard Library
we can discover new modules at the Python Module of the Week blog


Quiz: The Standard Library
Quiz: Compute an Exponent
It's your turn to import and use the math module. Use the math module to calculate e to the power of 3. print the answer.

Refer to the math module's documentation to find the function you need!'''

import random
import math

# print e to the power of 3 using the math module
'''print(math.exp(3))          # 20.085536923187668 (more precise)
print(math.pow(math.e, 3))  # 20.085536923187664
Quiz: Password Generator
Write a function called generate_password that selects three random words from the list of words word_list and concatenates them into a single string.

Your function should not accept any arguments and should reference the global variable word_list to build the password.

file: words.txt

click here to see words.txt
my solution: password_generator.py'''

# Use an import statement at the top

word_file = "words.txt"
word_list = []

# fill up the word_list
with open(word_file, 'r') as words:
    for line in words:
        # remove white space and make everything lowercase
        word = line.strip().lower()
    # don't include words that are too long or too short
    if 3 < len(word) < 8:
        word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words
# concatenated together without spaces


def generate_password():
    password = ""
    for _ in range(0, 3):
        password += random.choice(word_list)
    return password


# test your function
'''print(generate_password())
key method:

random.choice(word_list)
answer 1:

def generate_password():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)
answer 2:

use the random.sample function and .join method for strings
def generate_password():
    return ''.join(random.sample(word_list,3))
'''
