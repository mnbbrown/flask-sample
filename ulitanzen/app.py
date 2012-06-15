from flask import Flask, request,jsonify
from ulitanzen.config import Config
from ulitanzen.extensions import db, cache
from ulitanzen import routes
from ulitanzen.utils import RE

DEFAULT_BLUEPRINTS = [
	routes.events
]

def create_app():
	app = Flask(__name__)
	app.config.from_object(Config())
	configure_errorhandlers(app)
	configure_blueprints(app, DEFAULT_BLUEPRINTS)
	configure_extensions(app)
	return app

def configure_blueprints(app, blueprints):
	for blueprint in blueprints:
		app.register_blueprint(blueprint)

def configure_extensions(app):
    db.init_app(app)
    cache.clear()

def configure_errorhandlers(app):
	
	@app.errorhandler(404)
	def page_not_found(error):
		return jsonify(error='Sorry, page not found')
	    
	@app.errorhandler(403)
	def forbidden(error):
		return jsonify(error='Sorry, not allowed')
	    
	@app.errorhandler(500)
	def server_error(error):
		return jsonify(error='Sorry, an error has occurred')
	
	@app.errorhandler(501)
	def server_error(error):
		return jsonify(error='Not Implemented')
		
if __name__ == '__main__':
	create_app().run()