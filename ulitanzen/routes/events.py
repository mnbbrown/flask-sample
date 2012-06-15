from flask import Blueprint, request, jsonify, abort, render_template
from collections import OrderedDict
from ulitanzen.models import Event
from ulitanzen.extensions import db,cache

events = Blueprint('events', __name__, url_prefix="/events")

@events.route('', methods=['POST'])
def createEvent():
	if request.method == 'POST':
		
		print request.args['title']	
		event = Event(request.args['title'], request.args['description'], request.args['start_date'], request.args['end_date'])
		db.session.add(event)
		db.session.commit()
		#render_template('events.html', events=events)
		return jsonify(event=dict(event))	

@events.route('', methods=['GET'])
def listEvents():
	events = cache.get('all-events')
	if events is None:
		results = Event.query.all()
		events = []
		for event in results:
			events.append(OrderedDict(event))
		cache.set('all-events', events, timeout=5*60)		
	return jsonify(events=events)


@events.route('/<int:id>', methods=['GET','PUT','DELETE'])
def updateEvent(id):
	if request.method == 'GET':
		event = cache.get('event-'+str(id))
		if event is None:
			event = OrderedDict(Event.query.get_or_404(id))
			cache.set('event-'+str(id), event, timeout=5*60)
		return jsonify(event=event)
		
	elif request.method == 'PUT':
		
		abort(501)
		
	elif request.method == 'DELETE':
		event = Event.query.get(id)
		db.session.delete(event)
		db.session.commit()
		return ""