#!/usr/bin/env python
import sys

for line in sys.stdin:
	line = line.strip()
	key_value  = line.split("\t")
	if key_value[0].isdigit():
	    if len(key_value[0])>=3:
		key_in		= key_value[0]
		value_in	= key_value[1]
		print('%s\t2,%s' % (key_in, value_in))
	    else:
		key_in		= key_value[1]
		value_in	= key_value[0]
		print('%s\t1,%s' % (key_in, value_in))
