import random
from triads import *
quitProgram = False
userInput = ''

print('Welcome to triads \n')


while not quitProgram:

	print('Enter to begin')
	print('Q to quit')

	userInput = input('Please input command \n')

	if userInput is 'q' or userInput is 'Q':
		quitProgram = True
	elif userInput is '':
		print(C_Major.first)

	
