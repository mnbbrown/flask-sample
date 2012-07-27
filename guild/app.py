import os
from flask import Flask, jsonify
from guild.config import Config
from guild import routes
from guild.lib import db
from guild.lib import mail

DEFAULT_BLUEPRINTS = [
	routes.events,
	routes.organisations,
	routes.members,
	routes.register
]

def build_app():
	app = Flask(__name__)
	app.config.from_object(Config())
	configure_extensions(app)
	configure_errorhandlers(app)
	configure_blueprints(app, DEFAULT_BLUEPRINTS)
	return app

def configure_extensions(app):
	db.init_app(app)

def configure_blueprints(app, blueprints):
	for blueprint in blueprints:
		app.register_blueprint(blueprint)

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