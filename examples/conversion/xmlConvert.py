import csvmapper

parser = csvmapper.CSVParser('../mappers/record_example.csv', csvmapper.JSONMapper('../mappers/mapper_example.json'))
converter = csvmapper.XMLConverter(parser)

print converter.doConvert('example')