# Exercise 10-8 From 'Python Crash Course'
# 22-01-2026 G. Melief

# Exercise import and read files And using try-except block

from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"Can not find the file {path}.")
    else:
        print(contents)
