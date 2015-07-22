from flask import Flask, render_template
from util import flickr
import random

app=Flask(__name__)

tags=['Sloth','Platypus','Giraffe','Bonobo']

@app.route('/')
def root():
    #a=flickr(random.choice(tags))
    return render_template('photo.html', image=flickr(random.choice(tags)))


if __name__=='__main__':
    app.debug=True
    app.run()
