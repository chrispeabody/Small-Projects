# Chris Peabody
# String Generator
# generate.py
# Called the best darn generator ever by some guy once.

import random
import sys

# Connect to configuration file and list-ify it
if len(sys.argv) > 1:
	cfgfile = sys.argv[1]
	print("Generator connected. . .")
else:
	print("No generator configuration given. Please try again.")
	sys.exit(0)

cfg = file(cfgfile, 'r')
config = list(cfg)

for i in range(len(config)):
	config[i] = config[i].replace('\r\n','')

# Ooh, list-erious!

###############################
## GET INFORMATION FROM FILE ##
###############################

# Collect all the lists of words

numlists = config.count("LIST")
lists = [] # A list of the word lists

if numlists == 0:
	print("No LIST sections found. Please try again.")
	sys.exit(0)

for x in range(numlists):
	startindex = config.index("LIST") # Where to start looking from
	counter = 1	# Where in the list, relative to the start
	config[startindex] = "PROCESSED" # So the next iteration will find an unprocessed list

	wordlist = [] # The collected list of words, will be appended to 'lists' later

	while config[startindex+counter] != '':
		wordlist.append(config[startindex+counter].lower())
		counter += 1

		if len(config) < startindex+counter:
			break

	lists.append(wordlist)

print("Lists collected. . .")

if config.count("FORMULAS") == 0:
	print("No FORMULAS section found. Please try again.")
	sys.exit(0)
else:
	startindex = config.index("FORMULAS")
	counter = 1

	formulas = []

	while config[startindex+counter] != '':
		formulas.append(config[startindex+counter])
		counter+=1

		if len(config) < startindex+counter:
			break

print("Formulas collected. . .\n")

#######################
## PHRASE GENERATION ##
#######################

def createPhrase(section):
	passuplist = []

	if section.count(' ') > 0:
		parts = section.split(' ')
		for part in parts:
			passuplist.append(createPhrase(part))

	elif section.count('-') > 0:
		parts = section.split('-')
		together = ''
		for part in parts:
			together = together + createPhrase(part)
		passuplist.append(together)

	elif section[0] == '(' and section[len(section)-1] == ')':
		return section.strip('()')

	elif section[0] == '^':
		frombelow = createPhrase(section.lstrip('^'))

		frombelow = list(frombelow)
		frombelow[0] = frombelow[0].upper()
		frombelow = ''.join(frombelow)

		passuplist.append(frombelow)

	elif section.isdigit():
		passuplist.append(random.choice(lists[int(section)-1]))

	# Package it to pass up
	passup = ''
	for x in range(len(passuplist)):
		passup = passup + passuplist[x]
		if x != len(passuplist)-1:
			passup = passup + ' '

	return passup

print("To exit, type 'exit' instead of a number.")
userin = raw_input("Number of strings to generate: ")

while(userin.isdigit()):
	numphrases = int(userin)
	
	print('')

	for x in range(numphrases):
		ranFormula = random.choice(formulas)
		phrase = createPhrase(ranFormula)
		print(phrase),

		print('')

	print('')

	userin = raw_input("Number of strings to generate: ")