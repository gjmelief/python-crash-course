# Exercise 10-14 From 'Python Crash Course'
# 24-01-2026 G. Melief

# Exercise expanding 10-13

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

def check_username(path):
    # Check if username is correct
    information = get_stored_information(path)
    if information:
        # Check if username is correct, if not prompt for information
        username_correct = input(f"Is {information['username']} your name? y/n: ")
        if username_correct == "y":
            return True
    return False

def greet_user():
    '''Greet the user by name and display its information'''
    path = Path('information.json')

    if check_username(path):
        information = get_stored_information(path)
        print("This is what we have on you:")
        for k, v in information.items():
            print(f"    -{k.capitalize()}: {v.title()}")
        return

    information = get_new_information(path)
    print(f"We'll remember you when you come back, {information['username']}!")

greet_user()