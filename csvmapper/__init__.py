# =============================
#
# CSV-Mapper
# Copyright (C) Samarjeet Singh
#
# =============================

import sys

if sys.version_info[0] == 3:
    # the parser
    from csvmapper.csv_parser import CSVParser, CSVWriter
    # import all mappers
    from csvmapper.mapper import *
    # utils
    from csvmapper.utils import CSVObject
    # converter
    from csvmapper.converter import *
else:
    # the parser
    from csv_parser import CSVParser, CSVWriter
    # import all mappers
    from mapper import *
    # utils
    from utils import CSVObject
    # converter
    from converter import *
