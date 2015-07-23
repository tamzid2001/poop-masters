import urllib2
import json

def flickr(tag='Sloth'):
    url='https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=112e9e41ffbac9819b2f051401f0c48e&tags=%s&format=json&nojsoncallback=1'%tag
    u=urllib2.urlopen(url)
    result=u.read()
    w=json.loads(result)
    return w['photos']['photo']
