#!/usr/bin/env python
import sys

input_filename = sys.argv[1]
print "the name of the file is ", input_filename

input_file = open(input_filename, 'r')
for line in input_file:
	print line
input_file.close()
