# ------------------------
#
# Test CSV->Object Mapping
# Base Function
#
# ------------------------

import unittest
from csvmapper import CSVObject

class ObjectTest(unittest.TestCase):
	def setUp(self):
		d = { 'name' : 'john', 'age': 14, 'primes':[2, 3, 5, 7, 11]}
		self.object = CSVObject(d)

	def testObject(self):
		self.assertEqual(self.object.name, 'john')
		self.assertEqual(self.object.age, 14)

if __name__ == '__main__':
	unittest.main()