from flask.ext.mail import Mail, Message

mail = Mail()

def welcomeEmail():
	print "Sending Email!"
	
	msg = Message(
			  'Welcome the The Society Of Smart Investors',
		   sender='theteam@ssinvestors.com',
		   recipients=['mnbbrown+test@gmail.com'])

	msg.body = "This is the email body"
	mail.send(msg)

def resetEmail():
	print "Sending Reset Email"

	msg = Message(
			  'Reset Your Password',
		   sender='theteam@ssinvestors.com',
		   recipients=['mnbbrown+test@gmail.com'])

	msg.body = "This is the email body"
	mail.send(msg)