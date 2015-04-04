# tests type and parsing
import os
import unittest
import csvmapper

class BasicTest(unittest.TestCase):

	def setUp(self):
		csvFile = os.path.abspath('tests/data/sampleData.csv')
		mapper = csvmapper.XMLMapper(os.path.abspath('tests/data/mapper1.xml'))
		parser = csvmapper.CSVParser(csvFile, mapper)
		self.obj = parser.buildObject()

	def test_parse(self):
		self.assertEqual(self.obj[1].Name, 'Paul')

	def test_type(self):
		if self.obj != None:
			aType = type(self.obj[0].Age)
			self.assertEqual(aType, type(0))

if __name__ == '__main__':
	unittest.main()