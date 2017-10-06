from BeautifulSoup import BeautifulSoup 
import requests
import re

def get_lyrics(song):
    title = song.get_title();
    artist = song.get_artist();
    
    title = '-'.join(title.split(" "));
    artist = '-'.join(artist.replace("'", '').split(" "));
    
    url = 'https://genius.com/' + artist +'-' + title + '-lyrics';
    
    print url
    response = requests.get(url);
    html = response.content;
    
    soup = BeautifulSoup(html);
    
    lyrics_div = soup.find('div', attrs={'class' : 'lyrics'})
    
    if lyrics_div == None:
        return 'Song not found'
    
    lyrics_p = lyrics_div.find('p');
    
    lyrics = parse_lyrics(lyrics_p);
    return lyrics;

def parse_lyrics(lyrics):
    lyrics = re.sub('<([^>]*)>', '', lyrics.prettify());
    return lyrics