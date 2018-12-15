again = 'y'
while again.lower().strip() == 'y':
	#Get string to be converted from user
	str = input("Enter the string you would like to convert: ")

	print("Here is your conversion with each letter corresponding to it's" + \
		" binary equivalent:  ")
	#loop through characters first converting to unicode, then binary
	for char in str:
		print(char , ":" , format(ord(char), 'b'))


	one_line = input("Would you like to see your conversion all on one line? y/n  ")
	if one_line.lower().strip() == 'y':
		#Ask user if they'd like to seperate their characters by spaces 
		together = input("Would you like it to be separated by spaces? y/n  ")
		print("Here is your conversion on one line: ")
		if together.lower().strip() == 'y':
			print(' '.join(format(ord(char), 'b') for char in str))
		elif together.lower().strip() == 'n':
			print(''.join(format(ord(char), 'b') for char in str))					
	again = input("\nWould you like to convert another string to binary? y/n  ")

