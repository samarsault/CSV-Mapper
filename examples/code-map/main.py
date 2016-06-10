import math
import cProfile
import csvmapper

x = [
	[
		{ 'name':'length' ,'type':'int'},
		{ 'name':'breadth',  'type':'int'}
	],
	[
		{ 'name': 'radius' ,'type':'int'}
	]
]

mapper = csvmapper.DictMapper(x)
csv_file = 'simple.csv'
parser = csvmapper.CSVParser(csv_file, mapper)
objs = parser.buildObject()

for i in range(0, len(objs)):
	obj = objs[i]
	if i % 2 == 0:
		area = obj.length * obj.breadth
		print 'A rectangle with length %dcm and breadth %dcm has area %dcm' %(obj.length, obj.breadth, area)
	else:
		circumf = 2 * obj.radius * math.pi
		print 'A circle with radius %dcm has circumference %dcm' %(obj.radius, circumf)
