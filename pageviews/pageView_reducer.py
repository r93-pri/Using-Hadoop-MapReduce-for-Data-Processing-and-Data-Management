#!/usr/bin/env python
import sys

pageId_list=[]						# List to store pageIds
age_list=[]						# List to store Age
first_time = 1
for line in sys.stdin:
	line = line.strip()
	keys  = line.split("\t")
	if first_time == 1:				# Assign prev_key to the first userId only for the first time
		prev_key = keys[0]
		first_time = 0
	if keys[0]==prev_key:				# Append the pageIds and age for the same user
		key = keys[1].split(",")
		if key[0]=='1':
			pageId_list.append(key[1])	# Append pageIds
		else:
			age_list.append(key[1])		# Append age
	else:
		for pageId in range(len(pageId_list)):	# Print the values before moving onto the next user
			for age in range(len(age_list)):
				print('%s\t%s' % (pageId_list[pageId], age_list[age]))
		pageId_list=[]				# Clear the lists for the next user
		age_list=[]
		key = keys[1].split(",")
		if key[0]=='1':				# To capture the first entry for the next user. All the
			pageId_list.append(key[1])	# other entries are captured in the if condition above.
		else:
			age_list.append(key[1])		
		prev_key=keys[0]
for pageId in range(len(pageId_list)):			# Print the values of the last user
	for age in range(len(age_list)):
		print('%s\t%s' % (pageId_list[pageId], age_list[age]))
