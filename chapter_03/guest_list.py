# Oefening om te werken met lists
guests = ['ester', 'timo', 'matthias', 'michel', 'papa']
# Laat zien uit hoeveel personen de gastenlijst bestaat met de len functie
print(f'\nDe gastenlijst bestaat uit {len(guests)} personen')
print(f'\nHallo {guests[0].title()},\nHierbij nodig ik u uit om te komen dineren morgenavond.')
print(f'\nHallo {guests[1].title()},\nHierbij nodig ik u uit om te komen dineren morgenavond.')
print(f'\nHallo {guests[2].title()},\nHierbij nodig ik u uit om te komen dineren morgenavond.')
print(f'\nHallo {guests[3].title()},\nHierbij nodig ik u uit om te komen dineren morgenavond.')
print(f'\nHallo {guests[4].title()},\nHierbij nodig ik u uit om te komen dineren morgenavond.')

# Vervang een value in de list
print(f'\n{guests[0].title()} kan helaas niet komen')
guests[0] = 'mirjam'
print(f'\nHallo {guests[0].title()},\nHierbij nodig ik u uit om te komen dineren morgenavond.')
print(f'\nHallo {guests[1].title()},\nHierbij nodig ik u uit om te komen dineren morgenavond.')
print(f'\nHallo {guests[2].title()},\nHierbij nodig ik u uit om te komen dineren morgenavond.')
print(f'\nHallo {guests[3].title()},\nHierbij nodig ik u uit om te komen dineren morgenavond.')
print(f'\nHallo {guests[4].title()},\nHierbij nodig ik u uit om te komen dineren morgenavond.')

# Voeg meer values toe aan de list
# Aan het begin, in het midden en op het eind
print('\nIk heb een grotere tafel gevonden!')
guests.insert(0, 'tim')
guests.insert(4, 'rob')
guests.append('sven')
print(f'\nDe gastenlijst bestaat uit {len(guests)} personen')

# print de nieuwe uitnodigingen
print(f'\nHallo {guests[0].title()},\nHierbij nodig ik u uit om te komen dineren morgenavond.')
print(f'\nHallo {guests[1].title()},\nHierbij nodig ik u uit om te komen dineren morgenavond.')
print(f'\nHallo {guests[2].title()},\nHierbij nodig ik u uit om te komen dineren morgenavond.')
print(f'\nHallo {guests[3].title()},\nHierbij nodig ik u uit om te komen dineren morgenavond.')
print(f'\nHallo {guests[4].title()},\nHierbij nodig ik u uit om te komen dineren morgenavond.')
print(f'\nHallo {guests[5].title()},\nHierbij nodig ik u uit om te komen dineren morgenavond.')
print(f'\nHallo {guests[6].title()},\nHierbij nodig ik u uit om te komen dineren morgenavond.')
print(f'\nHallo {guests[7].title()},\nHierbij nodig ik u uit om te komen dineren morgenavond.')

# Verwijder een value uit de lijst
print(f'\nDe tafel is toch niet groot genoeg, ik kan maar twee mensen kwijt aan de tafel')
uninvited_guest = guests.pop()
print(f'\nSorry {uninvited_guest}, het feest gaat niet door')
uninvited_guest = guests.pop()
print(f'\nSorry {uninvited_guest}, het feest gaat niet door')
uninvited_guest = guests.pop()
print(f'\nSorry {uninvited_guest}, het feest gaat niet door')
uninvited_guest = guests.pop()
print(f'\nSorry {uninvited_guest}, het feest gaat niet door')
uninvited_guest = guests.pop()
print(f'\nSorry {uninvited_guest}, het feest gaat niet door')
uninvited_guest = guests.pop()
print(f'\nSorry {uninvited_guest}, het feest gaat niet door')
print('\n',guests)

print(f'\nDe gastenlijst bestaat uit {len(guests)} personen')

# Maak de lijst leeg met del
del guests[0]
del guests[0]
print(guests)

print(f'\nDe gastenlijst bestaat uit {len(guests)} personen')