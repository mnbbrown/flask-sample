from guild.lib.db import db
from datetime import datetime
from dateutil.parser import parse
from collections import OrderedDict
from flask import current_app

import Organisation

def seralizeDateTime(obj):
	if obj is None:
		return None
	return obj.strftime("%Y-%m-%d %H:%M")

class Event(db.Model):
	
	__tablename__ = 'events'

	id = db.Column(db.Integer, primary_key=True)
	organisation_id = db.Column(db.Integer, db.ForeignKey('organisations.id'))
	name = db.Column(db.String(80))
	location = db.Column(db.String(80))
	starttime = db.Column(db.DateTime)
	endtime = db.Column(db.DateTime)
	blurb = db.Column(db.String(255))
	active = db.Column(db.Boolean)

	def __init__(self, organisation_id, name, location, starttime, endtime, blurb=None, active=False):
		self.organisation_id = organisation_id
		self.name = name
		self.location = location
		self.starttime = starttime
		self.endtime = endtime
		self.blurb = blurb
		self.active = active

	def serialize(self, recurse=True):
		return OrderedDict([
			('id' , self.id),
			('organisation_id', self.organisation_id),
			('name' , self.name),
			('location' , self.location),
			('starttime' , seralizeDateTime(self.starttime)),
			('endtime' , seralizeDateTime(self.endtime)),
			('active', self.active)
		])