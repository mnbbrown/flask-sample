
import re

class RE:

	def __init__(self, pattern, flags=0):
		'do and save re.compile(pattern, flags)'
		self._pattern = re.compile(pattern, flags)

	def match(self, string, flags=0):
		'do, save, and return pattern.match(string, flags)'
		RE._match = self._pattern.match(string, flags)
		return RE._match

	def search(self, string, flags=0):
		'do, save, and return pattern.search(string, flags)'
		RE._match = self._pattern.search(string, flags)
		return RE._match

	def group(grp=0):
		'return match_object.group(grp)'
		return RE._match.group(grp)
	group = staticmethod(group)


class SR:

	def __or__(self, value):
		'save value as _ and return value'
		self._ = value
		return value

	def group(self, grp=0):
		'return _.group(grp)'
		return self._.group(grp)

if __name__ == '__main__':

	lines = []
	lines.append(' 1     one   ')
	lines.append(' two   2     ')
	lines.append(' three three ')
	lines.append(' 4     4     ')

	reIntStr = RE(r'^\s*(?P<Int>\d+)\s+(?P<Str>\S.*?)\s*$')
	reStrInt = RE(r'^\s*(?P<Str>\S.*?)\s+(?P<Int>\d+)\s*$')
	for line in lines:
		print '>>>', line
		if reIntStr.search(line):
			print 'Int:', RE.group('Int')
			print 'Str:', RE.group('Str')
			print
		elif reStrInt.search(line):
			print 'Str:', RE.group('Str')
			print 'Int:', RE.group('Int')
			print
		else:
			print '*** UNMATCHED ***'
			print

	print "The same as above, now in a thread safe manner\n"

	reIntStr = RE.compile(r'^\s*(?P<Int>\d+)\s+(?P<Str>\S.*?)\s*$')
	reStrInt = RE.compile(r'^\s*(?P<Str>\S.*?)\s+(?P<Int>\d+)\s*$')
	m = SR()
	for line in lines:
		print '>>>', line
		if m|reIntStr.search(line):
			print 'Int:', m.group('Int')
			print 'Str:', m.group('Str')
			print
		elif m|reStrInt.search(line):
			print 'Str:', m.group('Str')
			print 'Int:', m.group('Int')
			print
		else:
			print '*** UNMATCHED ***'
			print
