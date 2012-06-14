class Config(object):

	DEBUG = True
	
	SQLALCHEMY_DATABASE_URI = "mysql://dev:dev@localhost/ssi"
	SQLALCHEMY_ECHO = False
	
	SECRET_KEY = "secret"