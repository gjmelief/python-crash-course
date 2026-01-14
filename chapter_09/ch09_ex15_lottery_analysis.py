# Exercise 9-15 From 'Python Crash Course'
# 14-01-2026 G. Melief

# Exercise simulating how much iterations before a lottery ticket is won

from random import choice

# Create a list containing 10 numbers and 5 letters
sequence = []
for number in range(0, 10):
    sequence.append(number)

for i in range(5):
    letter = chr(97 + i)
    sequence.append(letter)

print(f"The sequence with characters is: {sequence}")

# Randomly select 4 characters from the sequence
my_ticket = []
while len(my_ticket) < 4:
    pulled_item = choice(sequence)

    if pulled_item not in my_ticket:
        print(f"We pulled {pulled_item}!")
        my_ticket.append(pulled_item)

# Print statement declaring the winning lottery numbers
print(f"My lottery ticket is {my_ticket}!")

# Pull numbers until my_ticket is winning
winning_ticket = []
loop_runs = 0 # Counter for amount of loop runs
while len(winning_ticket) < 4:
    pulled_item = choice(sequence)
    loop_runs += 1

    if pulled_item in my_ticket:
        winning_ticket.append(pulled_item)
        print(f"{pulled_item} is in your ticket!")

print(f"It took only {loop_runs} pulls")