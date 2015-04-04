[![Build Status](https://travis-ci.org/samarjeet27/CSV-Mapper.svg?branch=master)](https://travis-ci.org/samarjeet27/CSV-Mapper)
[![PyPI Downloads](https://img.shields.io/pypi/dm/csvmapper.svg)](https://pypi.python.org/pypi/csvmapper)
CSV Mapper
===
Easily manipulate csv files with python. Python Module capable of parsing CSV files against a pre-defined mapper file.

![CSV-Mapper](http://oi61.tinypic.com/2qds6s1.jpg)


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
