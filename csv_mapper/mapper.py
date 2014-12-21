import xml.etree.ElementTree as ET

class Mapper(object):
	""" An XML-Defined Mapper File for the CSV Parser"""
	def __init__(self, path):
		super(Mapper, self).__init__()
		self.path = path
		self.records = []

	# create a record from an element
	def createRecord(self, elem):
		recs = []
		for x in elem:
			rec = {}
			for a in x.attrib:
				rec[a] = x.attrib[a]
			recs.append(rec)
		return recs

	# parse the mapper
	def parseFile(self):
		tree = ET.parse(self.path)
		root = tree.getroot()
		j = len(root)
		while j > 0:
			j=j-1
			g = root[j]
			for record in g:
				self.records.append(self.createRecord(record))

	def getRecords(self):
		self.parseFile()
		return self.records

# Test File
def test():
	m = Mapper('mapper_example.xml')
	m.parseFile()
	for rec in m.records:
		print rec

if __name__ == '__main__':
	test()