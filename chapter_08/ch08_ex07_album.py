# Exercise 8-7 From 'Python Crash Course'
# 25-11-2025 G. Melief

# Exercise defining a function building a dictionary

def make_album(artist, album_title, song_count = None):
    if song_count is not None: # Test if song_count has a value
        return {'artist_name': artist, 'album': album_title, 'tracks': song_count}
    else:
        return {'artist_name': artist, 'album': album_title}

print(make_album('stones', 'black', 15))
print(make_album('metallica', 'lightning'))
print(make_album('maiden', 'fear', 10))