import csv
import random

with open ("quotes.csv", 'r') as file:
	reader = csv.reader(file)
	quotes = list(reader)
quotes1 = [[i[0], i[1]] for i in quotes]
quotes1 = quotes1[4:]

def getQuote():
	return random.choice(quotes1)

