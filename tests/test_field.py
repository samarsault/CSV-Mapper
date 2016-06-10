import unittest
import csvmapper

class FieldTest(unittest.TestCase):
	def setUp(self):
		parser = csvmapper.CSVParser('tests/data/sampleData.csv', csvmapper.FieldMapper(('name', 'job','country','age')))
		self.obj = parser.buildDict()

	def test_attr(self):
		self.assertEqual(self.obj[0]['name'], 'John')
		self.assertEqual(self.obj[1]['age'], '32')

if __name__ == '__main__':
	unittest.main()