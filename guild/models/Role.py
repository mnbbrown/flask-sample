from datetime import datetime
from dateutil.parser import parse
from collections import OrderedDict
from flask import current_app

from guild.lib.db import db
import Membership

class Role(db.Model):
	
	__tablename__ = 'roles'

	id = db.Column(db.Integer, primary_key=True)
	role = db.Column(db.String(80))

	membership = db.relationship("Membership", backref='role')

	def __init__(self, name):
		self.role = role

	def serialize(self):
		return OrderedDict([
			('id' , self.id),
			('name' , self.name),
			('events', self.events.count()),
			('members', self.members.count())
		])