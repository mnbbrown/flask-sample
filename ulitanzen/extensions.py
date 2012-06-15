from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.contrib.cache import MemcachedCache

db = SQLAlchemy()

def todict(self):
    def convert_datetime(value):
        return value.strftime("%Y-%m-%d %H:%M:%S")

    d = {}
    for c in self.__table__.columns:
        if getattr(self, c.name) is None:
            value = None
        elif isinstance(c.type, db.DateTime):
            value = convert_datetime(getattr(self, c.name))
        else:
            value = getattr(self, c.name)

        yield(c.name, value)
	
def iterfunc(self):
    """Returns an iterable that supports .next()
        so we can do dict(sa_instance)
    """
    return self.todict()

db.Model.todict = todict
db.Model.__iter__ = iterfunc

cache = MemcachedCache(['127.0.0.1:11211'])