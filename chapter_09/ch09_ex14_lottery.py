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
winning_ticket = []
while len(winning_ticket) < 4:
    pulled_item = choice(sequence)

    if pulled_item not in winning_ticket:
        print(f"We pulled {pulled_item}!")
        winning_ticket.append(pulled_item)

# Print statement declaring the winning lottery numbers
print(f"The winning lottery ticket is {winning_ticket}!")