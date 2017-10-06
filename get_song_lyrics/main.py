from webscraper import get_lyrics
from song import Song 

def request_song():
    song_title = raw_input("please enter a song title: ");
    song_artist = raw_input("please enter the artist: ");
    
    song = Song(song_title, song_artist);
    
    lyrics = get_lyrics(song);
    print lyrics

# Start of main function
def main():
    request_song();
    
    response = raw_input("search another song? [y/n]")
    
    while response == 'y':
        request_song();
        
    print 'Goodbye'
    
main()