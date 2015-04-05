# ------------------------
#
# Test functionality
# of the mapper file parser
#
# ------------------------

import os
import unittest
from csvmapper import XMLMapper

class MapperTest(unittest.TestCase):

	def setUp(self):
		m = XMLMapper('tests/data/mapper1.xml')
		self.Mapper = m

	def test_parse(self):
		self.Mapper.parseFile()
		self.assertEqual(self.Mapper.records, [[ { 'name' : 'Name' }, { 'name' : 'Job' }, { 'name' : 'Country'}, { 'type':'int', 'name' : 'Age'}]])

if __name__ == '__main__':
	unittest.main()