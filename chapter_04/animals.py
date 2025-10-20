# Maak een list met dieren
animals = ['hond', 'kat', 'muis', 'wolf', 'paard', 'rat', 'baardagaam']

# Output die dieren met een for loop
for animal in animals:
    print(f'Een {animal.title()} heeft vier poten')

# Output een zin na de for loop
print('Het wordt als onethisch gezien om deze dieren op te eten')

# Oefen met slices op de list animals
# Print de eerste drie items
print(f'De eerste drie items in animals zijn {animals[:3]}\n')

# Print de middelste drie items
print(f'De middelste drie items in animials zijn{animals[2:-2]}\n')

# Print de laatste drie items in de list
print(f'De laatste drie items in animals zijn{animals[-3:]}')