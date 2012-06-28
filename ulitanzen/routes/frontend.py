from flask import Blueprint, request, redirect, url_for, escape, abort

frontend = Blueprint('frontend', __name__)

@frontend.route('/', methods=['GET'])
def home():
	return redirect(url_for(".login"))

@frontend.route('/login', methods=['GET','POST'])
def login():  
	if request.method == 'POST':
		print request.form['username']
		session['username'] = request.form['username']
		return redirect(url_for(".home"))
	elif request.method == 'GET':
		return '''
			<form action="" method="post">
				<p><input type=text name=username>
				
				<p><input type=submit value=Login>
			</form>
			<span><a href=%s>Register</a></span>
		'''

@frontend.route('/logout')
def logout():
	# remove the username from the session if it's there
	session.pop('username', None)
	return redirect(url_for('.home'))
@frontend.route('/log', methods=['POST'])
def log():
	print request
	return abort(404)