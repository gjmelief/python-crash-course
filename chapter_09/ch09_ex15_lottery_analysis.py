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

# Save original sequence
original_sequence = sequence[:]

# Pull numbers until my_ticket is winning
winning_ticket = []
# Counter for amount of loop runs
loop_runs = 0
# Logic for pulling numbers and comparing to my_ticket
while winning_ticket != my_ticket:
    loop_runs += 1
    while len(winning_ticket) < len(my_ticket):
        pulled_item = choice(sequence)
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)
    print(f"The winning ticket is {winning_ticket}!")

    if len(winning_ticket) == 4 and winning_ticket != my_ticket:
        winning_ticket = []
        sequence = original_sequence[:]

print(f"It took only {loop_runs} pulls")