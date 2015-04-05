import unittest
import csvmapper

class WriterTest(unittest.TestCase):
	def setUp(self):
		parser = csvmapper.CSVParser('tests/data/withHeader.csv', hasHeader=True)
		self.obj = parser.buildDict()
		# object manipulation
		self.obj[0]['Name'] = 'Julie' # was Daisy

	def testWrite(self):
		writer = csvmapper.CSVWriter(self.obj)
		writer.write('tests/data/withHeader2.csv')

if __name__ == '__main__':
	unittest.main()