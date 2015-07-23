from flask import Flask, render_template, request
from util import flickr
#import xcodex
import random

app=Flask(__name__)

tags=['Sloth','Platypus','Giraffe','Bonobo']

@app.route('/', methods=['POST','GET'])
def root():
    #print tag
    if request.method=="GET":
        tag=flickr(random.choice(tags))
    elif request.method=="POST":
        tag=flickr(request.form['search'])
        #a = findsong(request.form['search'])
        #y = songmeaning(a)
    else:
        return 'yo'
    #tag=flickr(random.choice(tags))
    return render_template('photo.html', image=tag, x=random.randint(0,100))
#y=y


"""
if request.method == 'GET':
    return render_template( 'interface.html' )
        else:
            xinputx = request.form
                a = xinputx['artist']
        xfx = findsong(a)
        f_id = xfx['response']['songs'][0]['artist_foreign_ids'][0]['foreign_id']
        
            xfindx = xcodex.findsong(a)
            findid = xcodex.songid()
            meaningsong = xcodex.songj()
        
        return render_template('interface.html',x = meaningsong, j = f_id)
"""

if __name__=='__main__':
    app.debug=True
    app.run()
