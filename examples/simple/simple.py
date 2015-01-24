import csvmapper

csv_file = 'simple_record.csv'
mapper = csvmapper.XMLMapper('simple_mapper.xml')
parser = csvmapper.CSVParser(csv_file, mapper)

items = parser.buildObject()

for item in items:
	print '{ Name:%s, Job:%s, Age:%d }' %(item.Name, item.Job, item.Age)
	# ^^ Note %d is used for age