from datetime import datetime
from dateutil.parser import parse
from collections import OrderedDict
from flask import current_app

from guild.lib.cache import redis
from guild.lib.db import db
from sqlalchemy.orm.collections import attribute_mapped_collection
from sqlalchemy.ext.associationproxy import association_proxy

import Membership, Event
from utils import serializeObjs

class Organisation(db.Model):
	
	__tablename__ = 'organisations'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))

	_rel_membership = db.relationship('Membership', primaryjoin='Organisation.id==Membership.organisation_id', collection_class=attribute_mapped_collection('member'), cascade='all,delete-orphan', backref='organisation')
	members = association_proxy('_rel_membership', 'role', creator=(lambda member, role: Membership(member=member, role=role)))
	events = db.relationship('Event', backref='event', lazy='dynamic')

	def __init__(self, name):
		self.name = name

	def serialize(self, recurse=True):
		return OrderedDict([
			('id' , self.id),
			('name' , self.name),
			('members', serializeObjs(self.members) if recurse is not False else len(self.members)),
			('events', serializeObjs(self.events.all()) if recurse is not False else len(self.events.all()))
		])