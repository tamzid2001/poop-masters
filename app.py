from flask import Flask, render_template, request
from util import flickr
import xcodex
import random

app=Flask(__name__)

tags=['Sloth','Platypus','Giraffe','Bonobo']

@app.route('/', methods=['POST','GET'])
def root():
    #print tag
    if request.method=="GET":
        tag=flickr(random.choice(tags))
        y=''
    elif request.method=="POST":
        tag=flickr(request.form['search'])
        a = xcodex.findsong(request.form['search'],request.form['song'])
        y = xcodex.songmeaning(a)
    else:
        return 'yo'
    #tag=flickr(random.choice(tags))
    return render_template('photo.html', image=tag, x=random.randint(0,100), y=y)
#y=y


if __name__=='__main__':
    app.debug=True
    app.run()
