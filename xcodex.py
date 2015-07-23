import urllib2 as urllib
import json


def findsong(a,c):
	s = urllib.urlopen("http://developer.echonest.com/api/v4/song/search?api_key=2ZOPM4G1WVLM5CJ17&format=json&artist=%s&title=%s&bucket=id:songmeanings"%(a,c))
	_id = s.read()
	z = json.loads(_id)
        #print z['response']['songs'][0]['artist_foreign_ids']
        return z['response']['songs'][0]['artist_foreign_ids'][0]['foreign_id']


def songmeaning(b):
	w = urllib.urlopen("http://developer.echonest.com/api/v4/artist/biographies?api_key=2ZOPM4G1WVLM5CJ17&id="+b)
	#print w
	songm = w.read()
        p = json.loads(songm)
	return p['response']['biographies'][3]['text']


    
