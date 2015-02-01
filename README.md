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

Quick Start
---

A quick snippet to get you started -

```python

import csvmapper

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


License
---
The MIT License