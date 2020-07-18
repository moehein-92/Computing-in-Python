class Artist:
    def __init__(self, name, label):
        self.name = name
        self.label = label

class Song:
    def __init__(self, name, album, year, artist):
        self.name = name
        self.album = album
        self.year = year
        self.artist = artist

def get_song_string(song):
    result = '''"{0}" - {1} ({2})'''.format(song.name, song.artist.name, song.year)
    return result



taylor = Artist("Taylor Swift", "Big Machine Records, LLC")
lights = Artist("LiGHTS", "Warner Bros. Records Inc.")

song_1 = Song("You Belong With Me", "Fearless", 2008, taylor)
song_2 = Song("All Too Well", "Red", 2012, taylor)
song_3 = Song("Up We Go", "Midnight Machines", 2016, lights)
#Feel free to add code to test your code below.
print(song_1.album)
print(song_2.artist.label)
print(song_3.artist.name)
