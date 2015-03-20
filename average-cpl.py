#!/usr/bin/python

# average-cpl
# Developed By: Preshant Achuthan
# Fork Me on GitHub: github.com/engerium

# Imports
from __future__ import print_function
import sys
import os.path

# Variables
FILE_EXTENSION = sys.argv[2]
file_list = []


# Main function
def main():

	# Variable declarations
	average_list = []
	total_average = 0

	DIRECTORY = sys.argv[1]

	# Get list of files with that language
	search_dir(DIRECTORY)

	# Search each file for the average number of charaters per line
	for filename in file_list:
		# Read a file line by line and store it as a list
		file_data = open_file(filename)

		# Get average number of characters for each line and append to average_list
		try:
			average_list.append(count_average_char(file_data))
			print ("<" + str(count_average_char(file_data)) + ">", end=" ")
			print (filename)

		# Show error if unable to get average for that file
		except:
			print ("File will not be part of the counting algorithm")

	# Get sum of all the averages
	for average in average_list:
		total_average = total_average + average

	# Print average
	print ("\nGloabal Average (" + FILE_EXTENSION + "): " + str(total_average/len(average_list)) + "\n")


# Open files function
def open_file(filename):

	# Try to open the file
	try:
		# Read file line by line
		file = open(filename, "r")
		file_data = file.readlines()
		file.close()

		# Return list containing file lines
		return file_data

	# Error message if unable to read the file
	except:
		# Print error
		print ("Unable to open " + filename)

		# Return none
		return None


# Count average number of charaters for each line
def count_average_char(file_data):
	# Varible declarations
	characters = 0
	lines = len(file_data)

	# For each line count number of characters
	for line in file_data:
		characters = characters + len(line)

	# Return average number of characters per line
	return characters/lines


# Step for recursive file search
def step(ext, dirname, names):
	ext = ext.lower()

	for name in names:
		if name.lower().endswith(ext):
			file_list.append(os.path.join(dirname, name))


# Recursively search for all files in the directory
def search_dir(path):
	os.path.walk(path, step, FILE_EXTENSION)


# Calling of main function
if __name__ == '__main__':
	main()