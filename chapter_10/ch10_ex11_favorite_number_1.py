# Exercise 10-11_1 From 'Python Crash Course'
# 24-01-2026 G. Melief

# Exercise using json library

from pathlib import Path
import json

path = Path('fav_num.json')
contents = path.read_text()
fav_num = json.loads(contents)

print(f"I know your favorite number! It's {fav_num}.")