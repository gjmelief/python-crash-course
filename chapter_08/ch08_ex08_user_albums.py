# Exercise 8-8 From 'Python Crash Course'
# 25-11-2025 G. Melief

# Exercise defining a function building a dictionary with a while loop

print("Lets build a dictionary containing information about a album."
        "\nEnter the artist name and album name."
        "\n(input 'q' to quit)")

def make_album(artist, album_title):
    '''Build a dictionary containing artist and album title'''
    album_dictionary = {
            'artist_name': artist.title(),
            'album': album_title.title(),
            }
    return album_dictionary # This contains the value with the outcome of the function

# Use a while loop to collect album information
while True:
    artist = input('Enter the artist name: ')
    if artist == 'q':
        break

    album_title = input('Enter the title of the album: ')
    if album_title == 'q':
        break

    album_dict = make_album(artist, album_title)
    print(album_dict)