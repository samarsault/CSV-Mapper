import csv
import json

# Converts CSV to supported formats
class CSVConverter(object):
	"""CSVConverter(csvmapper.CSVParser)"""
	def __init__(self, parser):
		super(CSVConverter, self).__init__()
		self.parser = parser

	def doConvert(self):
		pass

class JSONConverter(CSVConverter):
	"""CSV->JSON Converter"""
	def __init__(self, parser):
		super(JSONConverter, self).__init__(parser)
		
	def doConvert(self, pretty=True, indent=4):
		dic = self.parser.buildDict()
		if pretty:
			return json.dumps(dic, indent=indent)
		else:
			return json.dumps(dic)

class XMLConverter(CSVConverter):
	"""CSV->XML Converter"""
	def __init__(self, parser):
		super(XMLConverter, self).__init__(parser)

	# thanks @reimund for this function
	def dict2xml(self, d, root_node=None):
		wrap = False if None == root_node or isinstance(d, list) else True
		root = 'objects' if None == root_node else root_node
		root_singular = root[:-1] if 's' == root[-1] and None == root_node else root
		xml = ''
		children = []

		if isinstance(d, dict):
			for key, value in dict.items(d):
				if isinstance(value, dict):
					children.append(self.dict2xml(value, key))
				elif isinstance(value, list):
					children.append(self.dict2xml(value, key))
				else:
					xml = xml + ' ' + key + '="' + str(value) + '"'
		else:
			for value in d:
				children.append(self.dict2xml(value, root_singular))

		end_tag = '>' if 0 < len(children) else '/>'

		if wrap or isinstance(d, dict):
			xml = '<' + root + xml + end_tag

		if 0 < len(children):
			for child in children:
				xml = xml + child

			if wrap or isinstance(d, dict):
				xml = xml + '</' + root + '>'
			
		return xml

	def doConvert(self, root=None):
		dic = self.parser.buildDict()
		return self.dict2xml(dic, root)

