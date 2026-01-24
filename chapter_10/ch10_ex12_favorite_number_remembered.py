# Exercise 10-12 From 'Python Crash Course'
# 24-01-2026 G. Melief

# Exercise using json library with logic

from pathlib import Path
import json

# A program that checks if there's a favorite number. If not, it asks for it.
path = Path('fav_num_remembered.json')
if path.exists():
    contents = path.read_text()
    fav_num = json.loads(contents)
    print(f"I know your favorite number! It's {fav_num}.")
else:
    fav_num = input("What is your favorite number? ")
    contents = json.dumps(fav_num)
    path.write_text(contents)
    print(f"I will remember your favorite number is {fav_num}.")