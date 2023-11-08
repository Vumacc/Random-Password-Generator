import random
import string

# Define the character sets for letters and numbers
letters = string.ascii_lowercase
numbers = string.digits

# Change the numbers to get more or less letters/numbers in the password
random_letters = [random.choice(letters) for _ in range (5)]
random_numbers = [random.choice(numbers) for _ in range(5)]

# Combines the letters and numbers into a single line
random_characters = random_letters + random_numbers

# Shuffles the characters to make it more random
random.shuffle(random_characters)

# Convert the list of characters into a string
password = ''.join(random_characters)

print(password)