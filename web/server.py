from flask import Flask, render_template, request
import code
server = Flask(__name__)

@server.route('/')
def root():
	#song_foreign = ccc.songid()
	"""
	if request.method == 'GET':
		return render_template('interface.html', x="")
	else:
		artistname = request.form
		a = artistname['artist']
	"""
	meaningsong = code.songj() 
	return render_template('interface.html',x = meaningsong)


if __name__ == '__main__':
	server.debug = True
	server.run()
