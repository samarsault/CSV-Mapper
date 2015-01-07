import csvmapper

csv_file = 'simple_record.csv'
mapper = 'simple_mapper.csv'
parser = csvmapper.CSVParser(csv_file, mapper)

items = parser.buildObject()

for item in items:
	print '{ Name:%s, Job:%s, Age:%d }\n' %(item.Name, item.Job, item.Age)
	# ^^ Note %d is used for age