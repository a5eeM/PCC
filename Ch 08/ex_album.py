def make_album(artist_name, album_title, number_of_tracks=""):
    """Build a dictionary containing information about an album."""
    album = {
        "artist": artist_name.title(),
        "album": album_title.title()
        }
    if number_of_tracks:
        album["number of tracks"] = number_of_tracks
    return album

album = make_album("Led Zepplin", "Led Zepplin")
print(album)
album = make_album("Led Zepplin", "Led Zepplin", 13)
print(album)
album = make_album("metallica", "master of puppets")
print(album)
album = make_album("pink floyd", "the wall", number_of_tracks=26)
print(album)
