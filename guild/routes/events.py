from flask import Blueprint, request, jsonify, abort, render_template, make_response, current_app
from guild.models import Event
import json

events = Blueprint('events', __name__, url_prefix="/events")

def jsonResponse(data):
	resp = make_response(json.dumps(data, indent=4))
	resp.status_code = 200
	resp.mimetype = 'application/json'
	return resp

@events.route('/', methods=['GET'])
def register():	
	events = Event.query.all()
	events = [ event.serialize() for event in events ]
	return jsonResponse(events)

@events.route('/<id>', methods=['GET'])
def login(id):
	event = Event.query.get_or_404(id).serialize()
	return jsonResponse(event)