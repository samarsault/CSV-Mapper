class CSVObject(object):
	""" Converts a Dictionary to Object """
	def __init__(self, d):
		self.d = d
		for a, b in d.items():
			if isinstance(b, (list, tuple)):
				setattr(self, a, [CSVObject(x) if isinstance(x, dict) else x for x in b])
			else:
				setattr(self, a, CSVObject(b) if isinstance(b, dict) else b)

	def attrib(self,x):
		return self.d[x]

	def attribs(self):
		return self.d.keys()