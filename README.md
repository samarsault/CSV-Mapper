[![Build Status](https://travis-ci.org/samarsault/CSV-Mapper.svg?branch=master)](https://travis-ci.org/samarsault/CSV-Mapper)
CSV Mapper
===
Easily manipulate csv files with python. CSV Mapper is a python Module capable of parsing CSV files against a pre-defined mapper file, as well as converting between them.

Installation
---
CSV-Mapper can be installed using pip or easy_install

```sh

$ pip install csvmapper

```

Another way, which installs the latest updated version is 

```sh
$ git clone http://github.com/samarjeet27/CSV-Mapper
$ cd CSV-Mapper
$ python setup.py install

```

Basic Usage
---
Using Field Mapper

```python
from csvmapper import FieldMapper, CSVParser

fields = ('firstName', 'lastName', 'age')

# if csv file already has a header, use CSVParser('data.csv', hasHeader=True) instead
parser = CSVParser('data.csv', FieldMapper(fields))

data = parser.buildObject() # or parser.buildDict() for a dictionary
```

A quick snippet to parse files using a dictionary mapper (with type support) -

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
people = parser.buildObject()
print '%s will be %d years old after 2 years' %(people[0].firstName, (people[0].age + 2))
```
if your file already as column headers and you don't worry about the type, you can use -

```python
csvmapper.CSVParser('data.csv', hasHeader=True)
```

Write CSV
---

```python
# create parser
parser = csvmapper.CSVParser()
dictionary = parser.buildDict() # manipulation works for dict only at the moment
# manipulate csv file
writer = csvmapper.CSVWriter(dictionary) # or CSVObject instance
writer.write('data.csv') # write(filename)
```

Convert CSV to JSON/XML
---

```python
import csvmapper
# using same vars as above
converter = csvmapper.JSONConverter(parser) # or csvmapper.XMLConverter
print converter.doConvert(pretty=True)
```

License
---
The MIT License
