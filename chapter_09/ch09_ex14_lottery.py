# Exercise 9-14 From 'Python Crash Course'
# 13-01-2026 G. Melief

# Exercise with importing classes from the standard library

from random import choice

# Create a list containing 10 numbers and 5 letters
sequence = []
for number in range(0, 11):
    sequence.append(number)

for i in range(5):
    letter = chr(97 + i)
    sequence.append(letter)

print(sequence)