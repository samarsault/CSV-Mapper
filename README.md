CSV Mapper
===

Python Module capable of parsing CSV files against a pre-defined mapper file.

Installation
---
CSV-Mapper can be installed using pip / easy_install

```sh

$ pip install csvmapper

```

Another way, which installs the latest updated version is 

```sh
$ git clone http://github.com/samarjeet27
$ cd CSV-Mapper
$ python setup.py install

```

Example Code
---
```python
import csvmapper

# create mapper instance
mapper = csvmapper.XMLMapper('mapper.xml')

# create parser instance
parser = csvmapper.CSVParser(csv_file, mapper)

# build object map
items = parser.buildObject()

cube_dimensions = items[0]
# calculate volume
volume = cube_dimensions.length * cube_dimensions.breadth * cube_dimensions.height

customer = items[1]
print 'Welcome customer no. %g %s %s' %(customer.id, customer.firstName, customer.lastName)
```

Mapper Format
---

A Mapper file is pre-defined file/code, currently csv mapper supports JSON, XML and Python Code as mapper formats,
however more can be added inheriting Mapper class

```xml
<?xml version="1.0" encoding="UTF-8"?>
<stream name="ml1" format="csv">
	<!-- A group can contain several records -->
    <group name="group_name">
    	<!-- Each line is treated as a record -->
        <record name="cuboid">
            <field name="length" type="int" />
            <field name="breadth" type="int" /> <!-- Each Line Contains Comma-Seperated Fields -->
            <field name="height" type="int" />
        </record> 
        <record name="customer">
        	<field name="ID" type="long" />
        	<field name="firstName" />
        	<field name="lastName" />
        </record>
    </group>
</stream>
```

CSV File
---

A CSV File for the above mapper file would be

```csv
23,12,10
7
10,3,17
56
```

License
---
The MIT License