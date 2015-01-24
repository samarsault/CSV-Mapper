import csv
import mapper
import utils

class CSVParser(object):
	"""CSV Parser capable of parsing against a pre-defined mapper file"""
	def __init__(self, csv_file, fmapper):
		super(CSVParser, self).__init__()
		self.csv_file = csv_file
		self.fmapper = fmapper
		
	def getRecords(self):
		return self.fmapper.getRecords()

	# parses a CSV file
	def parseCSV(self):
		with open(self.csv_file, 'rb') as csvfile:
			rdr = csv.reader(csvfile, delimiter='\t', quotechar='|')
			x = []
			for row in rdr:
				x.append(row[0].split(','))
			self.csvData = x
 	
 	# convert type
 	def convertType(self,to,val):
 		if to == '':
 			return val
		i = ''
		exec('i = %s(%s)' %(to,val))
		return i

 	# convert csv data to record
 	def toDict(self, cdat, rec):
 		d = {}
 		i = 0
 		for j in rec:
 			a = cdat[i]
 			if 'type' in j:
 				a = self.convertType(j['type'], a)
 			d[j['name']] = a
 			i= i+1
		return d

	def getIndex(self, x, l):
		if x > (l-1):
			return x%l
		return x

	def buildObject(self):
		try:
			self.csvData
		except:
			self.parseCSV()
		recs = self.getRecords()
		l = len(recs)
		objs = []
		for x in range(0, len(self.csvData)):
			i = self.getIndex(x, l)
			dic = self.toDict(self.csvData[x], recs[i])
			objs.append(utils.CSVObject(dic))
		return objs