CSV Mapper
===

Python Module capable of parsing CSV files against a pre-defined mapper file.

Installation
---
CSV-Mapper can be installed using pip or easy_install

```sh

$ pip install csvmapper

```

Another way, which installs the latest updated version is 

```sh
$ git clone http://github.com/samarjeet27
$ cd CSV-Mapper
$ python setup.py install

```

Basic Usage
---

A quick snippet to parse files with mapper -

```python

import csvmapper

# can use csvmapper.JSONMapper, csvmapper.XMLMapper or custom mappers also
mapper = csvmapper.DictMapper([
	[ 
		{ 'name': 'firstName' } , 
		{ 'name' : 'lastName' }, 
		{ 'name': 'age', 'type':'int' }
	]
])

# data.csv
# ------
# John,Doe,39
# James,Bond,29
# Harry,Potter,28

parser = csvmapper.CSVParser('data.csv', mapper)
objects = parser.buildObject()
print '%s will be %d years old after 2 years' %(objects[0].firstName, (objects[0].age + 2))
```

Convert CSV

```python
import csvmapper
# using same vars as above
converter = csvmapper.JSONConverter(parser) # or XMLConverter
print converter.doConvert(pretty=True)
```

License
---
The MIT License
