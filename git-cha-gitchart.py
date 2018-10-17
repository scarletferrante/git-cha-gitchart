import os
from os.path import expanduser

def run():
	# Get the author name from .gitconfig and print
	# Find gitconfig file ~/.gitconfig
	path = expanduser("~")
	print(path)
	os.chdir(path)
	# Open file
	file = open('.gitconfig', 'r')
	contents = file.read()
	file.close()
	# Read name entry
	contents_list = contents.split()
	#print("contents_list = ", contents_list)
	for word in contents_list:
		if word == "name":
			name = contents_list[contents_list.index(word) + 2]
	# Output it to the screen
	print("name = ", name)
	# If the author of the commit is you, plot it
	# Get the time stape of the commit
	# Plot a point at that time
	# Display

if __name__ == '__main__':
	run()

