import os
import re

# store name/gender data in a dictionary
# returns the dictionary for analysis
def getNames():

	filename = "names/yob"
	
	#data is a dictionary structure that
	#holds a name as a key
	#a size 2 int array as the value pair
	#int array has the first value to indicate gender
	#second value indicates the count

	data = dict()

	genderMap = {'M': 0, 'F':1}

	# traversing through the files
	for i in range(1880,2015): 
		
		text_file = open(filename + str(i) + ".txt")
		
		# read line by line
		for line in text_file: 
			line = line.split(',')
			name = line[0]
			gender = genderMap[line[1]]
			count = int(line[2])

			if not data.has_key(name):
				data[name]=[0,0]
			data[name][gender]=data[name][gender]+count
			
		text_file.close()
		
	return data

if __name__ == "__main__":
	getNames()
