class CSVObject(object):
	""" Converts a Dictionary to Object """
	def __init__(self, d):
		self.__dict__ = d

	def attrib(self,x):
		return self.d[x]

	def attribs(self):
		return self.d.keys()
