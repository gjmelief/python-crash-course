# Exercise 10-1 From 'Python Crash Course'
# 18-01-2026 G. Melief

# Exercise practicing import text from files

from pathlib import Path

path = Path('chapter_10/learning_python.txt') # Point path to file location
contents = path.read_text() # Read the content of the file
lines = contents.splitlines() # Return each line in a list

print("Print the contents of learning_python.txt in one string")
print(contents)

print("\nLoop over the list and print the contents of learning_python.txt")
for line in lines:
    print(line)