# Quote Quizzer
from sys import argv
from time import sleep
try:
	script,quotefilename = argv
except:
	quotefilename = raw_input("[*] Quotefile Name: ")
quotefile = open(quotefilename)

def ask_quotes(set_of_quotes):
	unknownquotes = []
	global unknownquotes
	for line in set_of_quotes:
		shit = line.replace('\\n', '\n').split('|')
		print "-----------------------------------------------------------"
		print "Act %s Scene %s | Speaker: %s" % (shit[0], shit[1], shit[2])
		print "Context: %s" % shit[3]
		lol = raw_input("Quote?: ")
		print "Quote: %s" % shit[4]
		examine = raw_input("Did you get it correct? Y/N: ")
		if examine != 'y':
			unknownquotes.append(line)
ask_quotes(quotefile)
while unknownquotes != []:
	print "##########\nNEXT ROUND\n##########"
	ask_quotes(unknownquotes)
print "##########\nWELL DONE!\n##########"
exit()