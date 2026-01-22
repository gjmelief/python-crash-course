# Exercise 10-10 From 'Python Crash Course'
# 22-01-2026 G. Melief

# Exercise import and read files, and using the count function

from pathlib import Path

def count_common_words(path, word):
    """Count the number of times a word exists in a text"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        # Count the approximate number of a word in the file:
        words = contents.lower()
        num_common = words.count(word)
        print(f"The file {path} has about {num_common} times the word '{word}' in it.")

filenames = ['ethics.txt', 'meditations.txt', 'republic.txt']
for filename in filenames:
    path = Path(filename)
    count_common_words(path, 'the')