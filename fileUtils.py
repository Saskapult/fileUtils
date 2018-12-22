import json
import os

class fileIO(object):  # File IO utility
	__shouldCreate = True

	# Initialize!
	def __init__ (self, filename):
		self.filename = filename

	# Tests if the file exists yet
	def exists(self):	
		return os.path.isfile(self.filename) 

	# Called when printed
	def __str__(self):
		infoDict = {'Priv.fileName': self.filename, 
			'Priv.shouldCreate': self.__shouldCreate}
		string = self.__constructString()
		return string
		
	# Read file, returns full file text
	def read(self):
		file = self.__tryOpen('r')
		thing = file.read()
		file.close()
		return thing

	# Write to file
	def write(self, stuff):
		file = self.__tryOpen('w')
		file.write(stuff)
		file.close()

	# Append to file
	def append(self, stuff):
		file = self.__tryOpen('a')
		file.write(stuff)
		file.close()

	# Read a json file
	def readJson(self):
		file = self.__tryOpen('r')
		data = json.load(file)
		file.close()
		return data

	# Write a json file
	def writeJson(self, jsonData):
		file = self.__tryOpen('w')
		json.dump(jsonData, file)
		file.close()

	# Constructs a string for the __str__ function
	def __constructString(lines):
		string = ''
		string += 'Class: '
		string += __name__
		string += '\n'
		for line in lines:
			string += '\t' + line
		return string

	# Try to open a file
	def __tryOpen(self, mode):
		try:
			file = open(self.filename, mode)
		except:
			if self.__shouldCreate:
				file = open(self.filename, 'w')
				file.write('\n')
			else:
				print('NOT ALLOWED TO MAKE FILE, CANNOT PROCEED')
		return file

	# Deletion function
	#def __del__(self):
		# Close the file if it is not closed (for whatever reason)
		#if not self.file.close:
			#self.file.close()