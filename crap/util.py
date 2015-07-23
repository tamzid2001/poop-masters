import urllib2
import json

def flickr(tag='Sloth'):
    url='https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=44b5c3dafd75b345edf09410ed6847e6&tags=%s&format=json&nojsoncallback=1'%tag
    u=urllib2.urlopen(url)
    result=u.read()
    w=json.loads(result)
    return w['photos']['photo']
