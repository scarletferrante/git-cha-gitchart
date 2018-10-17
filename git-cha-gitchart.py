import os

def run():
	# Get the author name from .gitconfig and print
	# Find gitconfig file
	# ~/.gitconfig

	# Open file
	path = input('Location of .gitconfig file: ')
	print(path)
	os.chdir(path)

	file = open('.gitconfig', 'r')
	contents = file.read()
	file.close()
	print(contents)

	# Read name entry
	
	# Output it to the screen
	# If the author of the commit is you, plot it
	# Get the time stape of the commit
	# Plot a point at that time
	# Display
	print("Hello World!")

if __name__ == '__main__':
	run()

