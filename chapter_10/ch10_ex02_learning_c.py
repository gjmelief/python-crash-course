# Exercise 10-2 From 'Python Crash Course'
# 21-01-2026 G. Melief

# Exercise practicing import text from files and replacing a word

from pathlib import Path

path = Path('chapter_10/learning_python.txt')
contents = path.read_text()
lines = contents.splitlines()

print("\nLoop over the list and print the contents of learning_python.txt."
      "\nWhile replacing 'Python' with 'C'.")
for line in lines:
    print(line.replace('Python', 'C'))