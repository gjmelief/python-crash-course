# Plekken die ik wil zien in de wereld
places = ['grand canyon', 'chinese wall', 'macchu pichu', 'tokyo', 'swiss alps', 'niagara falls']

# Print de locaties
print(places)

# Print de locaties gesorteerd zonder de list te veranderen
print(sorted(places))

# Bewijs dat de orginele list niet is veranderd
print(places)

# Reverse de list en print deze
places.reverse()
print(places)

# Reverse de list naar z'n orginele volgorde
places.reverse()
print(places)

# Sorteer de lijst alfabetisch (permanent) en output op het scherm
places.sort()
print(places)

# Sorteer de lijst in omgekeerd aflbatische volgorde (permanent) en output op het scherm
places.sort(reverse=True)
print(places)

# Gebruik de .pop() function
next_location = places.pop(0)
print(f'\nMijn volgende vakantie is naar {next_location}.\n')
print(places)