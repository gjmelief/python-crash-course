# Exercise 10-11_0 From 'Python Crash Course'
# 24-01-2026 G. Melief

# Exercise using json library

from pathlib import Path
import json

# A program that ask's for a favorite number and stores it an a file
fav_num = input("What is your favorite number? ")
path = Path('fav_num.json')
contents = json.dumps(fav_num)
path.write_text(contents)
print(f"I will remember your favorite number is {fav_num}.")