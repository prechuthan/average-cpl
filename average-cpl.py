#!/usr/bin/python

# average-cpl
# Developed By: Preshant Achuthan
# Fork Me on GitHub: github.com/engerium

# Imports


# Main function
def main():

	# Read a file line by line and store it as a list
	file_data = open_file("")

	print file_data


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
		print "Unable to open " + filename

		# Return none
		return None


# Calling of main function
if __name__ == '__main__':
	main()