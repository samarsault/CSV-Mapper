import csvmapper

# patient mapper
mapper = csvmapper.JSONMapper('patient.json')

parser = csvmapper.CSVParser('patients.csv', mapper)

patients = parser.buildObject()

for patient in patients:
	print '( %g ) %s is %d years old, and is suffering from %s' %(patient.ID, patient.Name, patient.Age, patient.Disease)