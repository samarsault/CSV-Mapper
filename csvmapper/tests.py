import csv_parser
import mapper
import utils

def runTest(name):
	if name == 'csv_parser':
		csv_parser.test()
	elif name == 'mapper':
		mapper.test()
	elif name=='utils':
		utils.test()

def runAll():
	print 'Util Tests'
	print '-'*10
	utils.test()
	print '\nMapper Test'
	print '-'*10
	mapper.test()
	print '\nParser Test'
	print '-'*10
	csv_parser.test()

def testParser():
	csv_parser.test()