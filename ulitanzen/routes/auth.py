from flask import Blueprint, request, redirect, url_for, escape, abort

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
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
			<span><a href="${url_for(".register")}">Register</a></span>
		'''

@auth.route('/logout')
def logout():
	# remove the username from the session if it's there
	session.pop('username', None)
	return redirect(url_for('.home'))

@auth.route('/register', methods=['GET','POST'])
def register():
	if request.method == 'POST':
		
	elif request.method == 'GET':
		