from flask import Blueprint, request, jsonify, abort, render_template
from collections import OrderedDict
from ulitanzen.models import Event
from ulitanzen.extensions import db

events = Blueprint('events', __name__, url_prefix="/events")

@events.route('', methods=['GET','POST'])
def createEvent():
	if request.method == 'POST':
		
		print request.args['title']	
		event = Event(request.args['title'], request.args['description'], request.args['start_date'], request.args['end_date'])
		db.session.add(event)
		db.session.commit()
		#render_template('events.html', events=events)
		return jsonify(event=Event.todict(event))	
		
	elif request.method == 'GET':
		
		results = Event.query.all()
		events = []
		for event in results:
			events.append(OrderedDict(event))
        return render_template('events.html', events=events)

@events.route('/<int:id>', methods=['GET','PUT','DELETE'])
def updateEvent(id):
	if request.method == 'GET':
		
		event = Event.query.get(id)
		print event
		return render_template('user.json', event=event)
		
	elif request.method == 'PUT':
		
		abort(501)
		
	elif request.method == 'DELETE':
		event = Event.query.get(id)
		db.session.delete(event)
		db.session.commit()
		return ""