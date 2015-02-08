import csvmapper

parser = csvmapper.CSVParser('../mappers/record_example.csv', csvmapper.JSONMapper('../mappers/mapper_example.json'))
converter = csvmapper.JSONConverter(parser)

print converter.doConvert(pretty=True)