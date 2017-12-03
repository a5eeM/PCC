def make_album(artist_name, album_title, number_of_tracks=""):
    """Build a dictionary containing information about an album."""
    album = {
        "artist": artist_name.title(),
        "album": album_title.title()
        }
    if number_of_tracks:
        album["number of tracks"] = number_of_tracks
    return album

while True:
    print("\nEnter details of the album")
    print("(enter 'q' to quit)")

    artist_name = input("\nArtist Name: ")
    if artist_name == "q":
        break

    album_title = input("\nAlbum Title: ")

    album = make_album(artist_name, album_title)
    print(album)
