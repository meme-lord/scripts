#domainchecker.py
import requests
from sys import argv

script,domainsfile = argv
domains = open(domainsfile, 'r')
for domain in domains:
	page = requests.get('http://data.alexa.com/data?cli=10&url=%s' % domain.rstrip()).text
	#print page
	try:
		rank = page.split('<REACH RANK="')[1].split('"/>')[0]
		print "%s\t%s" % (rank,domain.rstrip())
	except:
		pass
#http://data.alexa.com/data?cli=10&url=google.com