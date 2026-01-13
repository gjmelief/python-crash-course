# Exercise 9-14 From 'Python Crash Course'
# 13-01-2026 G. Melief

# Exercise with importing classes from the standard library

from random import choice

# Create a list containing 10 numbers and 5 letters
sequence = []
for number in range(0, 10):
    sequence.append(number)

for i in range(5):
    letter = chr(97 + i)
    sequence.append(letter)

# Randomly select 4 characters from the sequence
char_1 = choice(sequence)
char_2 = choice(sequence)
char_3 = choice(sequence)
char_4 = choice(sequence)

# Print statement declaring the winning lottery numbers
winning_ticket = f"{char_1}{char_2}{char_3}{char_4}"
print(f"The winning lottery ticket is {winning_ticket}!")