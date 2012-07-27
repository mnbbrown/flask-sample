
def serializeObjs(objs):
        l = []
        for i in objs:
            l.append(i.serialize(recurse=False))

        if len(l) <= 0:
        	return None
        else:
        	return l

def seralizeDateTime(obj):
	if obj is None:
		return None
	else:
		return obj.strftime("%Y-%m-%d %H:%M")