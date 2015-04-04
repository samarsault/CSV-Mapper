import glob
import unittest

def create_test_suite():
	test_file_strings = glob.glob('tests/test_*.py')
	module_strings = ['tests.'+str[6:len(str)-3] for str in test_file_strings]
	suites = [unittest.defaultTestLoader.loadTestsFromName(name) \
			for name in module_strings]
	testSuite = unittest.TestSuite(suites)
	return testSuite

testSuite = create_test_suite()
test_runner = unittest.TextTestRunner().run(testSuite)