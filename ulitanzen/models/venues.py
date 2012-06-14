from ulitanzen.extensions import db
from collections import OrderedDict
from datetime import datetime

class Venue(db.Model):
	__tablename__ = 'venues'
	
	def todict(r):
		def cdt(v):
			return v.strftime("%Y-%m-%d %H:%M:%S")
 
		d = OrderedDict()
		for c in r.__table__.columns.keys():
			if isinstance(getattr(r, c), datetime):
				d[c] = cdt(getattr(r, c))
			else:
				d[c] = getattr(r, c)
		return d
	
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	
	def __init__(self, name):
		self.name = name