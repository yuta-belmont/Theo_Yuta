import goodmorning as gm
import quotes

#welcome
print("Welcome to the Belmontverse. Proceed.")

#get user input

while 1:
	inp = str(input())
	inp = inp.lower()


	if inp == 'help':
		commands = ['help', 'exit', 'quit', 'quote', 'goodmorning']
		for c in commands[1:]: #help is first, remove it
			print(c)
	elif inp == "exit":
		break
	elif inp == "quit":
		break
	elif inp == "quote":
		quo = quotes.getQuote()
		print('"'+quo[0]+'"') #quote
		print('-'+quo[1]) #author
	elif inp == "goodmorning":
		gm.gm()
		quo = quotes.getQuote()
		print('"'+quo[0]+'"') #quote
		print('-'+quo[1]) #author

	else:
		print('Error, nonexistent command. Try "help"')

print("Goodbye, sir.")

