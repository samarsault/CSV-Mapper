""" 
	YAML Mapper Example
	This shows how to create your own mappers.
	requires PyYAML
	Install :
		$ pip install PyYAML
"""
import yaml
import csvmapper

""" Yaml Mapper file for csv-mapper based on DictMapper class """
class YamlMapper(csvmapper.DictMapper):
	"""Yaml mapper file for csvmapper"""
	def __init__(self, fileName):
		super(YamlMapper, self).__init__(self.parse(fileName))

	def parse(self, file):
		f = open('map.yaml').read()
		return yaml.load(f)

mapper = YamlMapper('map.yaml')

parser = csvmapper.CSVParser('data.csv', mapper)

for item in parser.buildObject():
	print '%s (Customer no. %g ) bought a %s' %(item.Name, item.ID, item.Item)