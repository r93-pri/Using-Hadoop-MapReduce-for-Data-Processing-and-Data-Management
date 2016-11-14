#!/usr/bin/env python
import sys
import re

regex = re.compile('[^a-zA-Z]')			# Regular expression needed to strip all non-alphabetic characters

for line in sys.stdin:
	line = line.strip()			# Strip the return characters
	line = line.lower()			# Convert all alphabet to lower cases
	keys = line.split()			# Split the line into words
	for key in keys:
		key = regex.sub('', key)	# Strip all non-alphabetic characters
		if len(key)>0:			# Ignore words which contained only special characters which were removed in the previous step
			key= key[:1]
			value=1
			print('{0}\t{1}'.format(key,value))

