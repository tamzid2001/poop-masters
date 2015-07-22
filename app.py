from flask import Flask, render_template
from util import flickr
import random

app=Flask(__name__)

tags=['Sloth','Platypus','Giraffe','Bonobo']

@app.route('/')
def root():
    tag=flickr(random.choice(tags))
    return render_template('photo.html', image=tag, title_img='arrpi.php?text='+tag[0]['title'])


if __name__=='__main__':
    app.debug=True
    app.run()
