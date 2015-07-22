import urllib2 as urllib
import json

"""
def findsong():
	s = urllib.urlopen("http://developer.echonest.com/api/v4/song/search?api_key=2ZOPM4G1WVLM5CJ17&format=json&artist=&title=creep&bucket=id:songmeanings")
	_id = s.read()
	return json.loads(_id)
"""

def songmeaning():
	w = urllib.urlopen("http://developer.echonest.com/api/v4/artist/biographies?api_key=2ZOPM4G1WVLM5CJ17&id=songmeanings:artist:200")
	print w
	songm = w.read()
	return json.loads(songm)

def songj():
	song_meaning = songmeaning()['response']['biographies'][3]['text']
	return song_meaning
"""                     
def songid():
	f_id = findsong()['response']['songs'][0]['artist_foreign_ids'][0]['foreign_id']
	return f_id
"""



    
