# Exercise 10-13 From 'Python Crash Course'
# 24-01-2026 G. Melief

# Exercise using json library and writing multiple pieces of information

from pathlib import Path
import json

def get_stored_information(path):
    """Get stored information if available"""
    if path.exists():
        contents = path.read_text()
        information = json.loads(contents)
        return information
    else:
        return None

def get_new_information(path):
    """Prompt for a new information"""
    username = input("What is your name? ")
    location = input("What is your location? ")
    age = input("What is your age? ")
    # Store information in a dictionary
    information = {}
    information['username'] = username
    information['location'] = location
    information['age'] = age
    # Place the information in a .json file
    contents = json.dumps(information)
    path.write_text(contents)
    return information

def greet_user():
    '''Greet the user by name and display its information'''
    path = Path('information.json')
    information = get_stored_information(path)
    if information:
        print("This is what we have on you:")
        for k, v in information.items():
            print(f"    -{k.capitalize()}: {v.title()}")
    else:
        information = get_new_information(path)
        print(f"We'll remember you when you come back, {information['username']}!")

greet_user()