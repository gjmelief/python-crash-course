# Exercise 5-6 From 'Python Crash Course'
# 04-11-2025 G. Melief

# Write if-elif-else chain that determines person's stage of life

# Set var 'age' for the age of the person
age = 70

# If age < 2, person stage is baby
if age < 2:
    stage = 'baby'
# If age < 4, stage is toddler
elif age < 4:
    stage = 'toddler'
# If age < 13, stage is kid
elif age < 13:
    stage = 'kid'
# If age < 20, stage is teenager
elif age < 20:
    stage = 'teenager'
# If age < 65, stage is adult
elif age < 65:
    stage = 'adult'
# If age >= 65, stage is elder
else:
    stage = 'elder'

# Print the message with the stage of the person's life
print(f'The person is a {stage}.')