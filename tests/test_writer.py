import unittest
import csvmapper
from copy import deepcopy

class WriterTest(unittest.TestCase):
	def setUp(self):
		self.parser = csvmapper.CSVParser('tests/data/withHeader.csv', hasHeader=True)
		self.obj = self.parser.buildDict()
		self.old = deepcopy(self.obj)
		# object manipulation
		for item in self.obj:
			item['SN'] = item['ID'] + '(' + item['Name'] + ')'
			item.pop('ID', None)
			item.pop('Name', None)

	def testWrite(self):
		writer = csvmapper.CSVWriter(self.obj)
		writer.write('tests/data/withHeader2.csv')
		obj = csvmapper.CSVParser('tests/data/withHeader2.csv', hasHeader=True).buildDict()
		old = self.old
		for i in range(0, len(obj)):
			a = obj[i]['SN']
			b = old[i]['ID'] + '(' + old[i]['Name'] + ')'
			self.assertEqual(a, b)

if __name__ == '__main__':
	unittest.main()
