#
# Test automatically generated mapper
# with hasHeader=True
#

import csvmapper
import unittest

class AutoMapper(unittest.TestCase):
	def setUp(self):
		self.parser = csvmapper.CSVParser('tests/data/withHeader.csv', hasHeader=True)

	def test_parse(self):
		customers = self.parser.buildObject()
		self.assertEqual(customers[1].Name, 'John')
		self.assertEqual(customers[3].Item, 'Macbook')