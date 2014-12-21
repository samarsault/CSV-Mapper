CSV Mapper
===

Python Module capable of parsing CSV files against a pre-defined mapper file.

Example Code
---
```python
import csv_mapper

parser = csv_mapper.CSVParser(csv_file, mapper_file)

items = parser.buildObject()

print items[0].length # see below first record will be cuboid and have length, breadth and height
print items[1].radius # see below second record will be a circle and have radius

```

Mapper Format
---

A Mapper file is a pre-defined xml file.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<stream name="ml1" format="csv">
	<!-- A group can contain several records -->
    <group name="group_name">
    	<!-- Each line is treated as a record -->
        <record name="cuboid">
            <field name="length"/>
            <field name="breadth"/> <!-- Each Line Contains Comma-Seperated Fields -->
            <field name="height"/>
        </record>
        <record name="circle">
        	<field name="radius"/>
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
