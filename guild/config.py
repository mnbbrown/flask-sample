class Config(object):

	DEBUG=True
	BASE_URL="http://localhost:5000/"

	#Database
	SQLALCHEMY_DATABASE_URI = "mysql://dev:dev@localhost/society"
	SQLALCHEMY_ECHO = True
	
	#Email
	MAIL_SERVER='smtp.gmail.com'
	MAIL_PORT=465
	MAIL_USE_SSL=True
	MAIL_USERNAME = 'theteam@ssinvestors.com'
	MAIL_PASSWORD = '@password22'

	#Celery
	CACHE_URL = 'redis://localhost:6379/0'